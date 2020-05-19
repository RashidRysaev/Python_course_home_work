    # task 3:
# Реализовать функцию ​my_func()​, которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

f_num = int(input('Введите величину первого аргумента: '))
s_num = int(input('Введите величину второго аргумента: '))
th_num = int(input('Введите величину третьего аргумента: '))

def my_func(f_num, s_num, th_num):
    my_list = [f_num, s_num, th_num]
    my_min = min(my_list)
    my_sum = sum(my_list)
    result = my_sum - my_min
    return result

answer = my_func(f_num, s_num, th_num)
print(answer)
