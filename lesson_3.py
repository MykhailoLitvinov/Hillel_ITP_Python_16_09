x = int(input("Введи целое число"))
if x > 0:
    y = 3
else:
    y = -1
print(y)

y = 3 if x > 0 else -1
print(y)

result = 7 if not x % 7 else 0
print(result)

my_value = 123.45678
my_str = f"my_value = {my_value}"
print(len(my_str))
print(my_str[5:3:-1])  # bad idea
new_str = my_str[4:6]
new_str = new_str[::-1]
print(new_str)
print(my_str[10])

index = 12
my_str = my_str[:index] + "_" + my_str[index + 1:]
print(my_str.upper())
value = '123@gmail.com'
if value.isdigit():
    print(int(value))
if value.isalnum():
    print("Это буквы или числа")

test_str = "qweR_tyuiOp"
if "i" in test_str:
    print("Такая подстрока есть!")

for symbol in test_str:
    if symbol not in 'eyuioa':
        print(symbol * 10)

for symbol in test_str:
    if symbol:
        print(symbol * 10)
