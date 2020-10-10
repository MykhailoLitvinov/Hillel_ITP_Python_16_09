from functions import generate_list_ip_address

number = 3
mask = "xx.xx.xx.x"
ip_list = generate_list_ip_address(number, repeat=False, sort=True)

print(ip_list)

open_file = open("Homeworks/lesson7.txt", "r")
for line in open_file.readlines():
    print("********")
    print(line)
    print("********")
open_file.close()

data = []
with open("sample.txt", "r") as open_file:
    # data = [line.strip() for line in open_file.readlines()]
    for line in open_file.readlines():
        data.append(line.strip())

print(data)