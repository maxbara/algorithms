
class DrawingCircleApiOne:

    def draw(self, x, y, radius):
        print('Using api 1, drawing circle on ({}, {}) with radius {}'.format(x, y, radius))

class DrawingCircleApiTwo:

    def draw(self, x, y, radius):
        print('Using api 2, drawing circle on ({}, {}) with radius {}'.format(x, y, radius))

class Circle:
    '''Bridge class for implementation-independent and implementation dependent operations'''

    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api
    
    def draw(self):
        self._drawing_api.draw(self._x, self._y, self._radius)

    def scale(self, percentage):
        self._radius *= percentage


circle1 = Circle(1, 2, 1, DrawingCircleApiOne())
circle1.draw()
circle1.scale(0.5)
circle1.draw()

circle2 = Circle(3, 4, 3, DrawingCircleApiTwo())
circle2.draw()
circle2.scale(0.685)
circle2.draw()

