    #task 5:
# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.



def sum_func(user_data):
    for i in user_data:
        user_data = list(map(int, user_data))
        result = sum(user_data)
        return result
answer = 0
while True:
    user_data = input('Enter some numbers: ').split()
    if user_data == ['q']:
        print('Program stopped')
        break
    elif ['q'] in user_data:
        answer.append(user_data)
        break
    else:
        answer = answer + sum_func(user_data)
        print(answer)

# не выходит последяя плюшка с отсечкой по спец.символу: все остальное работает