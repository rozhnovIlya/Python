# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return (f'{self.name} поехала')
    def stop(self):
        return (f'{self.name} остановилась')
    def turn_right(self):
        return (f'{self.name} повернула направо')
    def turn_left(self):
        return (f'{self.name} повернула налево')
    def show_speed(self):
        return (f'Скорость {self.name} состовляет {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость городского {self.name}  состовляет {self.speed}')
        if self.speed > 60:
            return (f'Скорость городского {self.name} превышенна')
        else:
            return (f'Скорость городского {self.name} не превышенна')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость рабочего {self.name}  состовляет {self.speed}')
        if self.speed > 40:
            return (f'Скорость рабочего {self.name} превышенна')
        else:
            return (f'Скорость рабочего {self.name} не превышенна')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)

audi = TownCar(100, 'красный', 'Q5', False)
opel = WorkCar(30, 'черный', 'astra', True)
lada = PoliceCar(150, 'белый', 'vesta', True)
ford = SportCar(200, 'желтый', 'mustang', False)
print(audi.color)
print(lada.turn_right())
print(audi.show_speed())
print(ford.show_speed())
print(opel.show_speed())

