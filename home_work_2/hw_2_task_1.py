    # task 1:
# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

some_str = 'Hello'
some_int = 3
some_list = [12, 'cap', -14.2, True]
some_tuple = ('chair', 7)
some_dict = {
    'name': 'Rocky',
    'age': 25
}

whole_list = [some_str, some_int, some_list, some_tuple, some_dict]

for l in whole_list:
    print(type(l))