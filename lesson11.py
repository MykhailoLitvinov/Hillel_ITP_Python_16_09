import requests
import json


def get_response(url):
    response = requests.get(url)
    return response.json()


def post_response(url, data):
    response = requests.post(url, data=data)
    return response.status_code

url_base = "http://54.37.125.181/api/v1/basic"
url_hello = f"{url_base}/hello-world/"
url_ip = f"{url_base}/get-my-ip/"
url_status = f"{url_base}/status/"
url_text = f"{url_base}/text/"
response = requests.get(url_status)
status_code = response.status_code
text = response.text
res_json = get_response(url_text)
print(json.dumps(res_json, indent=2))

data = {"text": "TEST TEXT"}
print(post_response(url_text, data))

res_json = get_response(url_text)
print(json.dumps(res_json, indent=2))

my_list = [1, 4, -5, 0]
sort_list = sorted(my_list, reverse=True, key=abs)
print(sort_list)

my_list = ["7", "4", "zasd", "-5", "!0", "zzz", "zxc"]
sort_list = sorted(my_list, key=len, reverse=True)
print(sort_list)
print(ord("!"), ord("A"))

def sort_key(tmp_dict):
    for key in tmp_dict:
        return key

my_list_dict = [
    {1945: "Окончание ВОВ"},
    {1991: "Независимость Украины"},
    {988: "Крещение Руси"}
]

my_list_dict = [
    {"name": "John", "age": 23},
    {"name": "John", "age": 13},
    {"name": "James", "age": 53},
    {"name": "Jack", "age": 18}
]


def sort_key(tmp_dict):
    return len(tmp_dict["name"]), tmp_dict["name"], tmp_dict["age"]


sort_dict = sorted(my_list_dict, key=sort_key)
print(sort_dict)

import re

my_str = "My e-mail: zontov_v2020@gmail.com.ua"
my_ip = "`dfhgajsgfjasj 123.234.56.1ajksf2736.4527.63.42hkshfkahf"
my_str_hw = "43 больше чем 34, но меньше чем 56"
my_hw = "2nd July 1961"


# reg_ex = r"[a-z0-9_]+@[a-z.]+"
# reg_ex = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
# reg_ex = r"[0-9]+"
reg_ex = r"[0-9]{1,2}[a-z]{2} [A-Z]{1}[a-z]+ [0-9]{4}"
result = re.findall(reg_ex, my_hw)  # СПИСОК
print(result)
# print(sum([int(i) for i in result]))
