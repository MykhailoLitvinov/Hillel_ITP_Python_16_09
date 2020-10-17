# from name_main import simple_func
#
# simple_func()

import json
import csv


def read_txt(filename_with_path):
    with open(filename_with_path, 'r') as txt_file:
        data = txt_file.read()
    return data


def read_json(filename_with_path):
    with open(filename_with_path, 'r') as json_file:
        data = json.load(json_file)
    return data


def read_csv(filename_with_path):
    with open(filename_with_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        data = [row for row in csvreader]
    return data


def file_reader(filename_with_path):
    mode = filename_with_path.rsplit(".")[-1]
    if mode == "txt":
        data = read_txt(filename_with_path)
    elif mode == "json":
        data = read_json(filename_with_path)
    elif mode == "csv":
        data = read_csv(filename_with_path)
    else:
        raise Exception("Unsupported file format!")
    return data


something = file_reader("test.csv")
print(something)
