    # task 2:
'''Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].'''

from random import randint


source_list = []
for i in range(12):
    source_list.append((randint(0, 100)))

new_source_list = [source_list[num] for num in range(1, len(source_list)) if source_list[num] > source_list[num - 1]]

print(source_list)
print(new_source_list)

# new_list = []
# for num in range(1, len(source_list)):
#     if source_list[num] > source_list[num - 1]:
#         new_list.append(source_list[num])
# print(new_list)
