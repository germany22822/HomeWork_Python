class Car:
    def __init__(self, speed, color, name, is_police = False, max_speed = 0):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.max_speed = max_speed
    def go(self):
        if self.speed > 0:
            return ' едет\n'
    def stop(self):
        if self.speed == 0:
            return 'остановка\n'
    def turn(self, direction):
        return 'поварачивает ' + direction + '\n'
    def MAX(self):
        if self.speed > self.max_speed:
            return 'выше максимальной скорости\n'
    
class TownCar(Car):
    def __init__(self, speed, color, name, is_police, max_speed):
        super().__init__(speed, color, name, is_police, max_speed)
        
class SportCar(Car):
    def __init__(self, speed, color, name, is_police, max_speed):
        super().__init__(speed, color, name, is_police, max_speed)
        
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, max_speed):
        super().__init__(speed, color, name, is_police, max_speed)
        
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, max_speed):
        super().__init__(speed, color, name, is_police, max_speed)
audi = SportCar(100, 'Red', 'Audi', False, 100)
Kia = TownCar(30, 'White', 'KIA', False, 60)
Ford = WorkCar(70, 'orange', 'Ford', False, 40)


Lada = PoliceCar(130, 'Black',  'Lada', True, 120)
print(f'марка {Lada.name},цвет {Lada.color},скорость {Lada.speed},полицейская {Lada.is_police}')
print(Lada.go(), Lada.turn('Право'), Lada.stop(), Lada.MAX())

