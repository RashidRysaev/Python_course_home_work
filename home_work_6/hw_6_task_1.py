    # task 1:
'''Создать класс ​TrafficLight ​(светофор) и определить у него один атрибут ​color ​(цвет) и метод running ​(запуск). 
Атрибут реализовать как приватный. 
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. 
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) ​— 2 секунды, 
    третьего (зеленый) — на ваше усмотрение. 
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).'''

from time import sleep


class TrafficLight:
    _color = 'red' or 'yellow' or 'green'

    def _running(self):
        while True:
            if TrafficLight._color == 'red':
                TrafficLight._color = 'yellow'
                sleep(7)
                print('Traffic lights are running red')
            elif TrafficLight._color == 'yellow':
                TrafficLight._color = 'green'
                sleep(2)
                print('Traffic lights are running yellow')
            elif TrafficLight._color == 'green':
                TrafficLight._color = 'red'
                sleep(5)
                print('Traffic lights are running green')


a = TrafficLight()
a._running()

