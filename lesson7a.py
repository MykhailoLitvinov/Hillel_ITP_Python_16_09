import random
from random import randint, choice


value = random.randint(1, 10)
print(value)
rand_list = [randint(1, 100) for _ in range(value)]
print(rand_list)
print(choice(rand_list))


# ФУНКЦИИ

def generate_random_list(number_list, min_val, max_val):
    return [randint(min_val, max_val) for _ in range(number_list)]

def special_print(min_value, max_value, coef):  # область видимости переменной
    print("ЭТО value ИЗ ТЕЛА ФУНКЦИИ:", coef)
    print("max_value: ", max_value)
    value = randint(min_value, max_value)
    print(f"This random value is {value}")
    return value * coef
value_1 = special_print(1, 10)  # позиционные аргументы (параметры)
value_2 = special_print(10, 100)
print(value_1, value_2)

coef = 10000
value_ = special_print(1, 10, coef)
print(value_)

number_list = randint(1, 10)
rand_list = generate_random_list(number_list, 20, 45)
print(rand_list)