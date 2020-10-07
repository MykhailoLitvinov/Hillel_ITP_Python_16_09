my_dict = {f"key_{a}": a ** 2 for a in range(7)}
tmp_dict = dict(key_10="qwe", key_0=1000)
print(tmp_dict)
my_dict.update(tmp_dict)
print(my_dict)

value = my_dict.pop("key_0")
print(value)
# d[100] = "Hello!"
value = my_dict.popitem()
print(value)
print(list(my_dict.items()))
print(list(my_dict.keys()))
print(list(my_dict.values()))

for key in my_dict:
    print(key, my_dict[key])

for key in my_dict.keys():
    print(key, my_dict[key])

for value in my_dict.values():
    print(value)

m_d = dict(a=1, b=2, c=1)
print(m_d.values())

for key, value in my_dict.items():
    print(key, value)

symbol_dict = dict(a=1, b=2, c=1)

symbol_dict["d"] = 5
symbol_dict.popitem()
print(symbol_dict.get("d"))
this_key = "z"

if this_key in symbol_dict.keys():
    print("--->", symbol_dict[this_key])
#
value = symbol_dict[this_key] if this_key in symbol_dict.keys() and symbol_dict[this_key] > 1  else -100
print("value = ", value)

# ПЛОХОЙ СПОСОБ!
try:
    print("--->", symbol_dict[this_key])
except KeyError:
    pass