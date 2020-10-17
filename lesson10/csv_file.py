import csv

# чтение из файла
# data = []
# with open("test.csv", 'r') as csvfile:
#     csvreader = csv.reader(csvfile)  # delimiter - параметр разделителя
#     # csvreader = csv.reader(csvfile, delimiter=";")  # delimiter - параметр разделителя
#     # print(csvreader)
#     # data = csvreader[1:]  # НЕ РАБОТАЕТ
#     # print(data)
#     for row in csvreader:  # считываем по строкам
#         # print(row)  # каждая строка - СПИСОК, заголовок тоже
#         data.append(row)
# header = data.pop(0)
# print(header)
# print(data)
#
# data.append(['qwe', 'wer', 'ert'])
# print(data)
# # запись файла
# with open('test_write.csv', 'w') as csvfile:
#     csvwriter = csv.writer(csvfile, delimiter=";")
#     csvwriter.writerow(header)
#     csvwriter.writerows(data)
#     csvwriter.writerow([10, None, 30, 40])


# чтение из файла
data = []
with open("test.csv", 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    # print(csvreader)
    for row in csvreader:   # считываем по строкам
        # print(type(row), dict(row))          # каждая строка - СЛОВАРЬ, ключи из заголовока
        data.append(row)    # список словарей
print(data)
# for row in data:
#     print(row["Third"])

if data:
    fieldnames = list(data[0].keys())
    with open("test_write.csv", 'w') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvwriter.writeheader()
        csvwriter.writerows(data)
