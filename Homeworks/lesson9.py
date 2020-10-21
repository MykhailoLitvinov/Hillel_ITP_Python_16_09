from datetime import datetime


def read_authors(filename):
    result = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            if "birth" in line.lower() or "death" in line.lower() or "died" in line.lower():
                result.append(line.strip())
    return result


def get_name(line):
    res_name = ''
    name = line.split("-")[-1]
    if "'s" in name:
        res_name = name.split("'s")[0].strip()
    elif " d" in name:
        res_name = name.split(" d")[0].strip()
    return res_name


def get_date_numbers(number_line):
    return "".join([symbol for symbol in number_line if symbol.isdigit()])


def get_date(line):
    date = line.split("-")[0].strip().split()
    date = f"{get_date_numbers(date[0])} {date[1]} {date[2]}"
    res_date = datetime.strptime(date, '%d %B %Y').strftime('%d/%m/%Y')
    return res_date


def get_author_dict_dummy(line):
    res_dict = {}
    res_dict["name"] = get_name(line)
    date = get_date(line)
    if "birth" in line.lower():
        res_dict["b_date"] = date
    elif "death" in line.lower() or "died" in line.lower():
        res_dict["d_date"] = date
    return res_dict if res_dict["name"] else {}


def get_author_dict(line: str) -> dict:
    res = {}
    dummy_dict = get_author_dict_dummy(line)
    if dummy_dict:
        res["name"] = dummy_dict["name"]
        res["date"] = dummy_dict.get("b_date") or dummy_dict.get("d_date")
    return res


def get_dict_list(lines):
    result_list = []
    for line in lines:
        res_dict = get_author_dict(line)
        if res_dict:
            result_list.append(res_dict)
    return result_list


print(get_dict_list(read_authors("authors.txt")))
