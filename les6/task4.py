class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала'

    def stop(self):
        return f'Машина {self.name} остановилась'

    def turn(self, direction):
        if direction == 'left':
            return f'Машина {self.name} повернула налево'
        if direction == 'right':
            return f'Машина {self.name} повернула направо'


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f'Скорость машины {self.name}: {self.speed} км/ч. Превышение скоростного режима!'
        else:
            return f'Скорость машины {self.name}: {self.speed} км/ч.'


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return f'Скорость машины {self.name}: {self.speed} км/ч. Превышение скоростного режима!'
        else:
            return f'Скорость машины {self.name}: {self.speed} км/ч.'


class SportCar(Car):

    def show_speed(self):
        return f'Скорость машины {self.name}: {self.speed} км/ч.'


class PolicetCar(Car):

    def show_speed(self):
        return f'Скорость машины {self.name}: {self.speed} км/ч.'


bmw_x7 = TownCar(60, 'Black', 'BMW X7', False)
audi_a8 = SportCar(120, 'Red', 'AUDI A8', False)
reno_logan = WorkCar(50, 'White', 'Renault Logan', False)
lada_vesta = PolicetCar(100, 'White-Blue', 'LADA Vesta', True)

print(bmw_x7.show_speed())
print(audi_a8.show_speed())
print(reno_logan.show_speed())
print(lada_vesta.show_speed())
