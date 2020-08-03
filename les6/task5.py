class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):

    def draw(self):
        return f'Рисую круг с помощью ручки {self.title}.'


class Pencil(Stationery):

    def draw(self):
        return f'Рисую квадрат с помощью карандаша {self.title}.'


class Handle(Stationery):

    def draw(self):
        return f'Рисую треугольник с помощью маркера {self.title}.'


stabilo = Pen('Stabilo')
koh_i_noor = Pencil('KOH-I-NOOR')
copic = Handle('Copic')

print(stabilo.draw())
print(koh_i_noor.draw())
print(copic.draw())
