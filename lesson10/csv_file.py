import csv

# чтение из файла
# data = []
# with open("lesson10/test.csv", 'r') as csvfile:
#     csvreader = csv.reader(csvfile)
#     print(csvreader)
#     # data = csvreader[1:]  # НЕ РАБОТАЕТ
#     # print(data)
#     for row in csvreader:  # считываем по строкам
#         print(row)  # каждая строка - СПИСОК, заголовок тоже
#         data.append(row)
# header = data.pop(0)
# print(header)
# print(data)
#
# data.append(['qwe', 'wer', 'ert'])

# запись файла
# with open('lesson10/test_write.csv', 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(header)
#     csvwriter.writerows(data)
#     csvwriter.writerow([10, 20, 30])


# чтение из файла
# data = []
# with open("lesson10/test_write.csv", 'r') as csvfile:
#     csvreader = csv.DictReader(csvfile)
#     print(csvreader)
#     for row in csvreader:   # считываем по строкам
#         print(type(row), dict(row))          # каждая строка - СЛОВАРЬ, ключи из заголовока
#         data.append(row)    # список словарей
# print(data)
# for row in data:
#     print(row["Third"])
