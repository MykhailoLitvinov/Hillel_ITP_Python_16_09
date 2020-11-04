import re


class TifFile:
    def __init__(self, text):
        self._text = text
        self._get_number_and_name()
        self._get_pages()

    def _get_number_and_name(self):
        last_line = self._text.rsplit("\n", 1)[-1]
        parts = sorted(last_line.split("="), key=len, reverse=True)
        self.filename = parts[0]
        self.number = parts[1].split("/")[0]

    def _get_pages(self):
        self.pages = []
        pages_lines = self._text.rsplit("\n", 1)[0]
        pages_lines = pages_lines.split("\n")
        pages_numbers = len(pages_lines) // 2
        for index in range(pages_numbers):
            page = Page(pages_lines[index + pages_numbers], pages_lines[index])
            self.pages.append(page)


class Page:
    def __init__(self, page_info, page_lines):
        self._page_info = page_info[1:-1]
        self._page_lines = page_lines
        self._parse_page_info()
        self._get_lines()

    def _parse_page_info(self):
        parts = re.findall(r"\d+", self._page_info)
        if len(parts) == 3:
            self.number = parts[0]
            self.height = parts[1]
            self.width = parts[2]

    def _get_lines(self):
        self.lines = re.findall(r"\[[^\[\]]*\]", self._page_lines)


def read_file(filename):
    with open(filename, "r") as file:
        data = file.read()
        data = data.split("\n\n")
    return data


filename = "lesson_15_data.txt"
data = read_file(filename)

result_list = []

for tif_file_data in data:
    tif_file = TifFile(tif_file_data)
    result_list.append(tif_file)

print(result_list[11].pages[-1].lines)
