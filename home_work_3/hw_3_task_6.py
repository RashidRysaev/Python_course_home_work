    # task 6:
# Реализовать функцию ​int_func()​, принимающую слово из маленьких латинских букв и
# возвращающую его же, но с прописной первой буквой. Например, ​print(int_func(‘text’))​ -> Text.
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию ​int_func()​.

# part 6.1:

word = input('Введите любое слово на латинице: ')

def int_func(text):
    word = text.title()
    return word

result = int_func(word)
print(result)

# part 6.2:

words = input('Введите слова на латинице через пробел: ').split()

def int_func_1(text):
    words = ','.join(text)
    words = words.title()
    return words

result = int_func_1(words)
print(result)

# не хватило времени закинуть две плюшки в одну функцию