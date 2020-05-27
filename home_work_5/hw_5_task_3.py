    # task 3:
'''Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). 
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32'''

list_less_than_20k = []
average_income = []

with open('task_3_file.rtf') as file:
    colleagues = file.read().split('\n')
    for el in colleagues:
        el = el.split()
        if float(el[1]) < 20000:
            list_less_than_20k.append(el[0])
        average_income.append(el[1])
        average_income_result = round(sum(map(float, average_income)) / len(average_income), 3)
    print(', '.join(list_less_than_20k))
    print(average_income_result)