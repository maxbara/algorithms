from abc import abstractmethod, ABC

class Person(ABC):

    @abstractmethod
    def greet():
        return ""

class Boss(Person):

    def greet(self):
        return "Hello, I'm the boss."

class Employee(Person):

    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello, my name is " + self.name

class Incomplete(Person):
    def __init__(self):
        pass

    def greet(self):
        pass


i = Incomplete()

p = Boss()

print(p.greet())

e = Employee("Max")

print(e.greet())

print(isinstance(e, Person))

print(isinstance(e, Employee))

