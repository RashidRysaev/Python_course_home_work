    # task 2:
# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def data_function(name, surname, birth_year, city, email, phone_num):
    print(f'Имя: {name}, Фамилия: {surname}, Д.Р.:{birth_year}, Город Проживания: {city}, Email: {email}, Ном. телефона: {phone_num}')

data_function(surname= 'Рюрикович', name= 'Игорь', birth_year= 878, city= 'Киев', phone_num= '+12345678910', email= 'igor_knyaz_of_Kiev@rurikovich.kr')