# task 2:
'''Реализовать проект расчета суммарного расхода ткани на производство одежды. 
Основная сущность (класс) этого проекта — ​одежда​, которая может иметь определенное название. 
К типам одежды в этом проекте относятся ​пальто ​и ​костюм​. 
У этих типов одежды существуют параметры: ​размер ​(для ​пальто​) ​и ​рост ​(для ​костюма​). 
Это могут быть обычные числа: ​V и H​, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: 
    для пальто (V/6.5 + 0.5)​, для костюма ​(2*H + 0.3)​. 
Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 
    реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора ​@property​.'''

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, V, H):
        self.V = V
        self.H = H

    @abstractmethod
    def coat_consumption(self):
        pass
        # return f'Amount of textile needed for production of one coat is {round(self.V / 6.5 + 0.5, 2)}'

    @abstractmethod
    def suit_consumption(self):
        pass
        # return f'Amount of textile needed for production of one suit is {2 * self.H + 0.3}'

    @property
    def common_consumption(self):
        return f'Total amount of textile needed is {round((self.V / 6.5 + 0.5) + (2 * self.H + 0.3), 2)}'

#
# cl = Clothes(10, 20) # запускается без проблем, но только тогда, когда я не указываю coat_ и suit_consumption как абстрактные
# print(cl.common_consumption)


class Coat(Clothes):
    def coat_consumption(self):
        return f'Amount of textile needed for production of one coat is {round(self.V / 6.5 + 0.5, 2)}'

    def suit_consumption(self):
        pass


class Suit(Clothes):
    def suit_consumption(self):
        return f'Amount of textile needed for production of one suit is {2 * self.H + 0.3}'

    def coat_consumption(self):
        pass


coat = Coat(5,7)
suit = Suit(7,5)
print(coat.coat_consumption())
print(suit.suit_consumption())


# написать в комменте, спросить, совместимы ли @property и @abstraction