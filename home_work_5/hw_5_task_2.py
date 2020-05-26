    # task 2:
'''Создать текстовый файл (не программно), 
сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.'''

with open ('task_2_file.rtf') as file:
    i = 0
    for line in file:
        i += 1
    print(i)

with open('task_2_file.rtf') as file:
    for line in file:
        print((len(line)))

# не могу подсчитать количество слов в каждой строке - только символов выходит