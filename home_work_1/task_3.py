# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

n = input("Введите любое число: ")
nn = int(n + n)
nnn = int(n + n + n)
n_sum = int(n) + nn + nnn
print(n_sum)