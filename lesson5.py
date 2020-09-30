REVERSE = True

my_str = 'blablacar'
my_symbol = "bla"
"""
1) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str. 
Напечатать столько раз my_symbol, сколько он встречается в my_str. 
Пример:  my_str="blablacar", my_symbol="bla". 
Вывод на экран:
bla
bla
"""
count = my_str.count(my_symbol)
# 1
text_symbol = my_symbol + '\n'
text = text_symbol * count
text = text.strip()
# 2
text_list = [my_symbol] * count
text = "\n".join(text_list)
print(text)
# 3
for _ in range(count):
    print(my_symbol)

print('-------------------------')
"""
2) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str. 
Напечатать ЧИСЛО сколько раз my_symbol встречается в my_str. 
Пример:  my_str="blablacar", my_symbol="bla". 
Вывод на экран:
2
"""
count = my_str.count(my_symbol)
print(count)
"""
3) У вас есть переменная my_str, тип - str. Напечатать ЧИСЛО сколько 
РАЗНЫХ символов встречается в my_str. 
Большая и маленькая буква считается как один символ. 
Пробелы, запятые и т.д. считаем тоже как символы.
Пример:  my_str="bla BLA car". 
Вывод на экран:
6
"""
my_str = "bla BLA carDDD"
lower_str = my_str.lower()
unique_str = ''
for symbol in lower_str:
    if symbol not in unique_str:
        unique_str += symbol
print(len(unique_str))


"""
4)
Дана строка my_str и пустой список my_list.
Заполнить my_list символами из my_str, 
которые стоят на четных местах в строке
"""

my_str = "qwerty"
my_list = []
# решение через приведение типов
# my_list = list(my_str[::2])
my_list.extend(list(my_str[::2]))
print(my_list)
# решение через цикл
for symbol in my_str[::2]:
    my_list.append(symbol)
print(my_list)

"""
5)
Дана строка my_str, список str_index целых чисел в диапазоне от 
0 до длинны строки минус 1, пустой список my_list.
Заполнить my_list символами из my_str, которые стоят на местах с 
индексами из str_index
"""
my_list = []
my_str = "qwerty"
str_index = [0, 5, 3, 3, 4]
for index in str_index:
    symbol = my_str[index]
    my_list.append(symbol)
    # my_list.append(my_str[index]) То же самое, но в одну строку
print(my_list)
"""
6)
Даны списки my_list_1 и my_list_2.
Создать список my_result в который поместить элементы из my_list_1 и 
my_list_2 через один.
a) кол-во эл-тов одинаковое
б) кол-во эл-тов разное
"""
my_list_1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
my_list_2 = [3, 4, 5, 6, 7, 8]
my_result = []

if len(my_list_2) < len(my_list_1):
    my_list_1, my_list_2 = my_list_2, my_list_1

list_len = len(my_list_1)
for index in range(list_len):
    my_result.append(my_list_1[index])
    my_result.append(my_list_2[index])
    # my_result.extend([my_list_1[index], my_list_2[index]])
my_result.append('')
my_result.extend(my_list_2[list_len:])
print(my_result)
"""
7)
Даны списки my_list_1 и my_list_2.
Создать список my_result в который вначале поместить 
элементы на четных местах из my_list_1, 
а потом все элементы на нечетных местах из my_list_2.
"""
my_result = my_list_1[::2] + my_list_2[1::2]
print(my_result)

"""
8)
Дано целое число. Определить сколько цифр в этом числе.
"""
number = 746527310
print(len(str(number)))
"""
9)
Дано целое число. Определить наибольшую цифру в этом числе.
"""
number = 7465279310
print(max(str(number)))

"""
10)
Дано целое число. Составить число с цифрами в обратном порядке.
"""
number = 746527310
print(int(str(number)[::-1]))
"""
11)
Дано целое число. Составить число с цифрами в порядке возрастания(убывания).
"""
number = 746527310
numb_list = list(str(number))
numb_list.sort(reverse=REVERSE)
str_numb = ''.join(numb_list)
new_numb = int(str_numb)
print(new_numb)
# сортировка списка
my_list = [3, 5, -6]
my_list.sort()
print(my_list)

# сортировка копии списка
new_list = sorted(my_list)
print(my_list)
print(new_list)
# порядок списка

"""
Цикл с условием(while)
Игра с угадыванием числа.

"""
mind_number = 34
number = int(input("Угадай число"))
while number != mind_number:
    try:
        if number < mind_number:
            number = int(input("Надо больше!"))
        else:
            number = int(input("Надо меньше!"))
    except:
        number = int(input("Введи целое число"))
print("Молодец, угадал!!!!")


solved = False
while not solved:
    try:
        number = int(input("Веди число"))
        if number < mind_number:
            number = print("Надо больше!")
        elif number > mind_number:
            number = print("Надо меньше!")
        else:
            solved = True
    except:
        pass
print("Молодец, угадал!!!!")
