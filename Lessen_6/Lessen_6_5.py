# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут
# title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self, title):
        Stationery.__init__(self, title)
    def draw(self):
        print(f'{self.title} отлично пишет в тетради')


class Pencil(Stationery):
    def __init__(self, title):
        Stationery.__init__(self, title)
    def draw(self):
        print(f'{self.title} отлично рисует в альбоме')


class Handle(Stationery):
    def __init__(self, title):
        Stationery.__init__(self, title)
    def draw(self):
        print(f'{self.title} отлично пишет на доске')

stationery_1 = Stationery('концелярская принадлежность')
pen_1 = Pen('Ручка')
pencil_1 = Pencil('Карандаш')
handle_1 = Handle('Маркер')

stationery_1.draw()
pen_1.draw()
pencil_1.draw()
handle_1.draw()

