# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_user = int(input("Введите время в секундах: "))
time_in_hours = time_user // 3600
remainder = time_user % 3600
time_in_minutes = remainder // 60
time_in_seconds = remainder % 60

print(f"Результат равен: {time_in_hours}:{time_in_minutes}:{time_in_seconds}")
