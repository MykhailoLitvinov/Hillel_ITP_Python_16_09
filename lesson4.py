value = input("Введите число")

# Проверка через if не всегда хорошее решение
if value != 0.0:
    result = 1 / value
else:
    result = None

# Обработка ошибки
try:
    value = float(value)
except:
    print("Не корректный ввод")
    value = 0.0
print(value)
try:
    result = 1 / value
except:
    print("На ноль делить нельзя!")
    result = None
print(result)
# Обработка ошибки с указанием типа ошибки
try:
    value = float(value)
    result = 1 / value
except ValueError:
    print("Не корректный ввод")
    result = None
except ZeroDivisionError:
    print("На ноль делить нельзя!")
    result = 0.0
print(result)
value = None
try:
    value = float(value)
    result = 1 / value
except (ValueError, ZeroDivisionError):
    print("Что-то не так!")
    result = None

# Структуры данных
# Кортеж - tuple
tuple_1 = (1, 3, "5", 8, "abc")
tuple_2 = (4, 8)
tuple_3 = (tuple_1, tuple_2)

print(tuple_1, type(tuple_1), len(tuple_1))
print(tuple_2[1])
print(tuple_3)

for value in tuple_1[2:-1]:
    print(value)

a = 5
b = 7
a, b = b, a
print(a, b)

# Распаковка кортежей
# a, b, c = tuple_2
val_1, *asjdhfgajsdja = tuple_1
print(asjdhfgajsdja)

# Список - list
print('----------------------------')
list_1 = [1, 3, "5", 8, "abc"]
list_2 = [4, 8]
list_3 = [list_1, list_2]
list_2[1] = 100
print(list_1, type(list_1), len(list_1))
print(list_2[1])
print(list_3)

tmp_value_none = list_1.append(list_2)
# print(tmp_value_none)
list_1.append("list_2")
list_1.append(len)
tmp_value = list_1.pop()
print("tmp_value:", tmp_value)
list_1.pop()
print(list_1)

print(tmp_value(list_2))

list_1.extend(list_2)
list_1.pop(5)
print(list_1)

my_str_list = []

for value in list_1:
    value = str(value)
    my_str_list.append(value)
    # my_str_list.append(str(value))

print(my_str_list)

result_str = "/".join(my_str_list)

print('4' in my_str_list)

# Пример решения предыдущего ДЗ
value = input()

if value in ["01", "03", "05", "07", "08", "10", "12", "январь"]:
    print("31")
elif value in ["04", "06", "11"]:
    print("30")
