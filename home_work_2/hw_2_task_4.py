    # task 4:
# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

user_info = input('Введите несколько слов, разделенных пробелами: ')

user_info_split = user_info.split()

for i, el in enumerate(user_info_split, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. - {el}")