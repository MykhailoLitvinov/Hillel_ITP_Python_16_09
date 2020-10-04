my_list = [-8, 1, 20, 34, 12, -8, 12, 1, 1, 23]
# возести в квадрат элементы на четных местах и остальные оставить без изменения

for index in range(len(my_list)):
    if index % 2 == 0:
        print(my_list[index] ** 2)
    else:
        print(my_list[index])

for index, value in enumerate(my_list):
    if index % 2 == 0:
        print(value ** 2)
    else:
        print(value)

# Возвести элемент списка в степень его индекса

for index, value in enumerate(my_list):
    print(value ** index)

# В new_list поместить числовые значения из my_list (в виде int), учитывая что числа могут быть строкой
my_list = [1, 2, 3, '4', '5', 6, 7, 'qwe', "88"]
new_list = []

for value in my_list:
    try:
        value = int(value)
        new_list.append(value)
    except ValueError:
        pass

for value in my_list:
    if type(value) == str:
        if value.isdigit():
            value = int(value)
            new_list.append(value)
    else:
        new_list.append(value)

print(new_list)

# Множество Set

my_set = set('my_listlistlist')
print(my_set)

"""
3) У вас есть переменная my_str, тип - str. Напечатать ЧИСЛО сколько
РАЗНЫХ символов встречается в my_str.
Большая и маленькая буква считается как один символ.
Пробелы, запятые и т.д. считаем тоже как символы.
Пример:  my_str="bla BLA car".
Вывод на экран:
6
"""
my_str = "bla BLA car"
print(len(set(my_str.lower())))

my_set_1 = {1, 2, 3, 7}
my_set_2 = {2, 3, 4}
my_set_1.add(7)
# 1
inter = my_set_1.intersection(my_set_2)
two_inter = inter
print(inter, my_set_1, inter is my_set_1)
# 2
my_set_1.intersection_update(my_set_2)
print(my_set_1)
#3
union = my_set_1.union(my_set_2)
print(union)
#4
my_set_1.update(my_set_2)
print(my_set_1)
# 5
dif = my_set_1.difference(my_set_2)
print(dif)
# 6
print(my_set_1)
# 7
sym_dif = my_set_1.symmetric_difference(my_set_2)
print(sym_dif)
#8
my_set_1.symmetric_difference_update(my_set_2)
print(my_set_1)

my_alphabet = ''
index_a = ord('Z')
print(index_a, chr(index_a - 1))

for index in range(ord('A'), ord('Z') + 1):
    my_alphabet += chr(index)
print(my_alphabet)
my_random = ''.join(set(my_alphabet))
print(my_random)
my_random = ''.join(set(my_random[::-1]))
print(my_random)

# Генератор списков

my_list = [1, 2, -3, 4, -5]
my_sqr = [value ** 2 for value in my_list]  # new object
print(my_sqr)
[print(value ** 2) for value in my_list]

# Знакомство со словарями dict

childrens = ["Nastya", "Vlada", "Matvey"]


person_zontov = {"name": "Vava",
          "age": 41,
          "childrens": childrens,
          "teacher": True,
                 12: "key_12"}

math_dict = {0: "Четное число",
             1: "Нечетное число"}

hillel_teachers = {"Zontov": person_zontov,
                   "Kaminsky": {}}

# print(math_dict[123%2])
print(hillel_teachers["Zontov"]["childrens"])