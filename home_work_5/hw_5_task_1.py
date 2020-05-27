    #task 1:
''' Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. 
Об окончании ввода данных свидетельствует пустая строка. '''


with open('task_1_file.rtf', 'w+') as file:
    while True:
        content = input('Enter some content: ')
        file.writelines(content + '\n')
        if not content:
            break



with open('task_1_file.rtf') as file:
    line = file.readlines()
    print(line)
