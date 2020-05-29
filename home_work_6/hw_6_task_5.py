    # task 5:
'''Реализовать класс ​Stationery ​(канцелярская принадлежность). 
Определить в нем атрибут ​title (название) и метод ​draw ​(отрисовка). 
Метод выводит сообщение “Запуск отрисовки.” 
Создать три дочерних класса ​Pen ​(ручка), ​Pencil ​(карандаш), ​Handle ​(маркер). 
В каждом из классов реализовать переопределение метода ​draw​. 
Для каждого из классов метод должен выводить уникальное сообщение. 
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationery():
    title = 'the_best_stationery'

    def draw(self):
        print('Drawing starts')

st = Stationery()
print(st.title)
st.draw()

class Pen(Stationery):

    def draw(self):
        print('Shall we draw with a pen?')

pn = Pen()
pn.draw()

class Pencil(Stationery):

    def draw(self):
        print('Or shall we take a pencil instead?')

pncl = Pencil()
pncl.draw()

class Handle(Stationery):

    def draw(self):
        print('I think we better go with a handle')

hndl = Handle()
hndl.draw()