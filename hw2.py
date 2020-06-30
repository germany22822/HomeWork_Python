class Road:
    def __init__(self, _length, _width, _gravity, _thickness):
        self.length = _length
        self.width = _width
        self.gravity = _gravity
        self.thickness = _thickness
    def voulume(self):
        return self.length * self.width * self.thickness * self.gravity
r = Road(5000, 20, 25, 0.005)
print(r.voulume())                          
