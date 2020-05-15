    # task 2:
# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

some_list = []

while len(some_list) < 5:
    some_list_user = input('Enter an element: ')
    some_list.append(some_list_user)

user_list = some_list

if len(user_list) % 2 == 0:
    i = 0
    while i < len(user_list):
        el = user_list[i]
        user_list[i] = user_list[i+1]
        user_list[i+1] = el
        i += 2
else:
    i = 0
    while i < len(user_list) - 1:
        el = user_list[i]
        user_list[i] = user_list[i + 1]
        user_list[i + 1] = el
        i += 2

print(user_list)