    # task 4:
'''Реализуйте базовый класс ​Car​. У данного класса должны быть следующие атрибуты: ​speed​, color​, ​name​, ​is_police ​(булево). 
А также методы: ​go​, ​stop​, ​turn(direction)​, которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: ​TownCar​, ​SportCar​, ​WorkCar​, ​PoliceCar​. 
Добавьте в базовый класс метод show_speed​, который должен показывать текущую скорость автомобиля. 
Для классов TownCar ​и ​WorkCar ​переопределите метод ​show_speed​. 
При значении скорости свыше 60 (​TownCar​) и 40 (​WorkCar​) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Выполните вызов методов и также покажите результат.'''

class Car:
    def __init__(self, speed, colour, name, is_police):
        self.car_speed = speed
        self.car_colour = colour
        self.car_name = name
        self.bool = is_police

    def go(self):
        print('Car goes')

    def stop(self):
        print('Car stops')

    def turn(self, direction):
        if direction == 'right':
            print('Car is turning right')
        elif direction == 'left':
            print('Car is turning left')

    def show_speed(self, speed):
        print(speed)

c = Car(80, 'green', 'Impala', False)
print(c.car_speed)
c.show_speed(12)

class TownCar(Car):

    def show_speed(self, speed):
        if speed > 60:
            print('Watch the speed limit - above 60!')
        else:
            print('Speed is OK')

tc = TownCar(50, 'blue', 'VW', False)
tc.show_speed(65)

class SportCar(Car):

    def sport_car(self):
        print('Origins from Car')

sc = SportCar(200, 'red', 'Bugatti', False)
print(sc.bool)

class WorkCar(Car):

    def show_speed(self, speed):
        if speed > 40:
            print('Watch the speed limit - above 40!')
        else:
            print('Speed is OK')

wc = WorkCar(25, 'yellow', 'Smart', False)
wc.show_speed(47)

class PoliceCar(Car):

    def police_car(self):
        print('Origins from Car')

pc = PoliceCar(90, 'black-white', 'Ford', True)
print(pc.bool)
