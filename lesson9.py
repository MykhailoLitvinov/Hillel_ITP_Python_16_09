import time
import sys


def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


def gaus_sum(number):
    result = 0
    for i in range(1, number + 1):
        result += i
    return result

run_func = {"f": factorial,
            "g": gaus_sum}

if len(sys.argv) > 2:
    func = sys.argv[1]
    number = int(sys.argv[2])
    result = run_func[func](number)
    print(result)


def get_run_time(function):
    start_time = time.time()
    function(60000)
    stop_time = time.time()
    print(stop_time - start_time)

get_run_time(gaus_sum)


def my_func(*args, **kwargs):
    for val in args:
        print(val)
    print('-----------------')
    print(kwargs)


my_func(1, "234", (1, 3, 4), **{"zxc": 1, "qwer": 4}, qwe=1, asd=4)

my_list = [1, 2, 3, 4, 5]
print(*my_list, sep=', ')

dict_1 = {"as":1, "zx":2}
dict_2 = {"as":"w", 1: 3}
dict_3 = {**dict_1,  **dict_2}
print(dict_3)


################################################
import os

path = "Homeworks"
list_dir = sorted(os.listdir(path))
print(list_dir) #   Не возвращает путь к объектам!!!
files = []
folders = []

for item in list_dir:
    path_item = os.path.join(path, item)
    if os.path.isfile(path_item):
        files.append(path_item)
    else:
        folders.append(path_item)

print(files)
print(folders)

path = f"Homeworks/{list_dir[1]}"
path = os.path.join("Homeworks", list_dir[1])
print(os.path.isfile(path))

################################################
# 1. Создать строку из маленьких букв, которая содержит весь английский алфавит.

# 2. Создать папку ./alphabet/ или проверить, что папка существует.

# 3. В папку ./alphabet/ поместить файлы вида a.txt, b.txt, ..., z.txt в которых будет записана строка алфавита, но с заменой буквы из названия файла на прописную. Пример: для b.txt строка будет aBcde...

# 4. Сделать щелчек Таноса 🙂  - удалить случайным образом половину всех файлов в этой папке.

import string
import os

alphabet = string.ascii_lowercase


if not os.path.isdir("alphabet"):
    os.mkdir("alphabet")

def write_file(filename: str, data: str):
    with open(filename, 'w') as file:
        file.write(data)


def do_tanos_click(path):
    list_dir = os.listdir(path)
    list_dir = [file for file in list_dir if os.path.isfile(os.path.join(path, file))]
    list_dir = list(set(list_dir))[:len(list_dir) // 2]
    [os.remove(os.path.join(path, file)) for file in list_dir]


try:
    os.mkdir("alphabet")
except FileExistsError:
    pass

for symbol in alphabet:
    filename = os.path.join("alphabet", f"{symbol}.txt")
    write_file(filename, alphabet.replace(symbol, symbol.upper()))

do_tanos_click("alphabet")


################################################
data = ["TEST", "LINE", "123"]
with open("test.txt", "w") as file:
    file.write("\n".join(["TEST", "LINE", "123"]))
    # for line in data:
    #     file.write(f"{line}\n")