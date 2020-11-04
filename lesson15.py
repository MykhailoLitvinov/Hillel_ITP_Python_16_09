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

print(result_list[10].number)