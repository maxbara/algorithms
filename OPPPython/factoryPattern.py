
class Dog:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Woof!"

class Cat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Meow!"
    


def get_pet(pet):

    pets = dict(dog=Dog("Doggy"), cat=Cat("Catty"))

    return  pets[pet]


dog = get_pet("dog")

print(dog.speak())

cat = get_pet("cat")

print(cat.speak())
