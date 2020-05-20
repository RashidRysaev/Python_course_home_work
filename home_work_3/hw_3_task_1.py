    # task 1:
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

f_num = float(input('Введите первое число: '))
s_num = float(input('Введите второе число: '))

def division(f_num, s_num):
    try:
        return f_num / s_num
    except ZeroDivisionError:
        return 'Деление на ноль!'

my_div = division(f_num, s_num)
print(my_div) # так ошибку при делении на 0 не выдает, исключение работает

# print(round(my_div, 2)) # так выдает, т.к. str не поддерживает round()
