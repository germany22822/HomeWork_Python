class Clothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def Full(self):
        return str(f'ткани на всё {(round(self.width / 6.5 + 0.5)) + (round(self.height * 2 + 0.3))}см2')
    
class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.Area_Coat = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Ткани на пальто {self.Area_Coat}см2'


class Jacket(Clothes):
    def __init__(self, height, width):
        super().__init__(height, width)
        self.Area_Jacket = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Ткани на костюм {self.Area_Jacket}см2'

a = 7
b = 1
#--------------:
C = Coat(a, b)
J = Jacket(b, a)
CL = Clothes
#--------------:
print(C)
print(J)
print(J.Full)

