import copy

class Prototype:

    def __init__(self):
        self.objects = dict()

    def register_object(self, name, obj):
        self.objects[name] = obj
    
    def unregister_object(self, name):
        del self.objects[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self.objects[name])
        obj.__dict__.update(attr)
        return obj

class Car:
    def __init__(self):
        self.name = "Tesla"
        self.color = "Red"
        self.rims = "21inch"

    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.rims)


car = Car()
prototype = Prototype()
prototype.register_object("Tesla", car)

clone = prototype.clone("Tesla")

print(clone)

clone2 = prototype.clone("Tesla", color = "black", rims = "19inch")

print(clone2)