
class Director:
    ''' Director '''

    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()  

    def get_car(self):
        return self._builder.car

class Builder:
    ''' Abstract Builder'''

    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class MercedesBuilder(Builder):
    ''' Concrete Builder -> provides parts and tools to work the parts '''

    def add_model(self):
        self.car.model = "G-Wagon"

    def add_tires(self):
        self.car.tires = "Goodyear"

    def add_engine(self):
        self.car.engine = "V12"

class Car:
    ''' Product '''
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return '{} | {} | {}'.format(self.model, self.tires, self.engine)

director = Director(MercedesBuilder())

director.construct_car()

car1 = director.get_car()

print(car1)


