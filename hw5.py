class Stationery:
    Title = 'Title'
    def draw(self):
        print('Запуск отрисовки.')
class Pen(Stationery):
    def draw(self):
        print('Отрисовка - ручка')
class Pencil(Stationery):
    def draw(self):
        print('Отрисовка - карандаш')
class Handle(Stationery):
    def draw(self):
        print('Отрисовка - маркер')

p = Pen()
pl = Pencil()
h = Handle()
p.draw()
pl.draw()
h.draw() 
