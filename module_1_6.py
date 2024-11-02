# Работа со Словарями:
my_dict = {"Anatoliy": 2000, "Vyacheslav": 1991, "Dmitriy": 1993}
print(my_dict)
existing_value = my_dict["Vyacheslav"]
print(existing_value)
not_existing_value = my_dict.get("Andrey")
print(not_existing_value)
my_dict.update({"Kirill": 1999,
               "Vitaly": 1987})
value_deleted = my_dict.pop("Anatoliy")
print(value_deleted)
print(my_dict)
# Работа с Множествами:
my_set = {"Orange", 12, "Green", 3, 12,3}
print(my_set)
my_set.add(10)
my_set.add(33)
my_set.remove("Orange")
print(my_set)
