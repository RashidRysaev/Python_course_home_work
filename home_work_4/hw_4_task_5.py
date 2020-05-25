    #task 5:
'''Реализовать формирование списка, используя функцию r​ange() и возможности генератора. 
В список должны войти четные числа от 100 до 1000 (включая границы). 
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию r​educe().​'''

from functools import reduce


def product(elem1, elem2):
    return elem1 * elem2


my_list = [num for num in range(100,1001,2)]


print(reduce(product, my_list))

