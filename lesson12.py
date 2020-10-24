from random import randint
from lesson12_bbox import Bbox, PathInfo

person = {"name": "John", "age": 24, "sex": "male"}
# print(person["name"])


# class Person:
#     name = "John"
#     age = 24
#     sex = "male"
#
#
# person_1 = Person()
# person_2 = Person()
# person_1.name = "Bill"
# person_1.age = 17
# print(person_1.name, person_1.age, person_1.sex)
# print(person_2.name, person_2.age, person_2.sex)

#################################################

# class Person:
#     planet = "Earth"  # Атрибут класса
#
#     def __init__(self, name, age, sex):
#         self.name = name  # Атрибут экземпляра класса
#         self.age = age
#         self.sex = sex
#
#     def age_increase(self):
#         self.age += 7
#
#
# person_1 = Person("John", 23, "male")
# person_2 = Person("Sveta", 7, "female")
# # person_1.name = "Vasya"
# # Person.planet = "Mars"
# # Person.name = "QQQ"
# # print(person_1.name, person_1.age, person_1.sex, person_1.planet)
# # print(person_2.name, person_2.age, person_2.sex, person_2.planet)
#
# for _ in range(randint(1, 10)):
#     person_1.age_increase()
#
# print(f"{person_1.name} теперь {person_1.age}")
# print(f"{person_2.name} теперь {person_2.age}")


# bbox_1 = Bbox(0, 0, 2, 3)
# bbox_2 = Bbox(1, 2, 3, 4)
# # print(bbox_1.w, bbox_1.h)
# # area = bbox_1.get_area()
# # print(area)
# print(bbox_1)
# bbox_list = [bbox_1, bbox_2]
# bbox_3 = bbox_1 + bbox_2
# print(bbox_3)

path_info = PathInfo("Homeworks")
print(path_info.show_folders())