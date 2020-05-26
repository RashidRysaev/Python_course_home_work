    # task 4:
'''Создать (не программно) текстовый файл со следующим содержимым:
One — 1 
Two — 2 
Three — 3 
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.'''

num_russian = {'One': 'Один', 'Two': 'Два', 'Three':'Три', 'Four':'Четыре'}
file_new = []

with open('task_4_file.rtf') as file:
    for i in file:
        i = i.split(' ', 1)
        file_new.append(num_russian[i[0]] + ' ' + i[1])
    print(file_new)

with open('task_4_file_new.rtf', 'w') as file_result:
    file_result.writelines(file_new)