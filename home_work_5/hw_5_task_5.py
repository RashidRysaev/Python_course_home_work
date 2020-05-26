    # task 5:
'''Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''

with open('task_5_file.rtf', 'w') as file:
    data = input('Enter some space-separated numbers: ')
    file.writelines(data)
    numbers = data.split()
    result = sum(map(int,numbers))
    print(result)