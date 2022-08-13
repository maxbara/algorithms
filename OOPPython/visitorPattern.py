
class House:
    ''' House to be visited by technicians '''
    
    def accept(self, visitor):
        ''' Accepts visitor and triggers the visitor'''
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, 'worked on by', hvac_specialist)

    def work_on_electricity(self, electrician):
        print(self, 'worked on by', electrician)

    def __str__(self):
        return self.__class__.__name__

class Visitor:
    '''Abstract/base class for visitor'''

    def __str__(self):
        return self.__class__.__name__

class HvacSpecialist(Visitor):
    '''Hvac visitor'''
    def visit(self, house):
        house.work_on_hvac(self)

class Electrician(Visitor):
    '''Electrician visitor'''
    def visit(self, house):
        house.work_on_electricity(self)


hvac = HvacSpecialist()
e = Electrician()
house = House()

house.accept(hvac)

house.accept(e)

