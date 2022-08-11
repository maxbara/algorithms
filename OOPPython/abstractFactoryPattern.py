from abc import ABC, abstractclassmethod

class Pet(ABC):

    @abstractclassmethod
    def speak(self):
        pass

class Dog(Pet):

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"

class Cat(Pet):

    def speak(self):
        return "Meow!"

    def __str__(self):
        return "Cat"
    
class PetFactory(ABC):

    @abstractclassmethod
    def get_pet(self) -> Pet:
        pass

    @abstractclassmethod
    def get_food(self) -> str:
        pass

class DogFactory(PetFactory):

    def get_pet(self) -> Pet:
        ''' intantiates dog '''

        return Dog()

    def get_food(self) -> str:
        ''' returns dog food object '''

        return "Dog food!"

        
class CatFactory(PetFactory):

    def get_pet(self):
        ''' intantiates cat '''

        return Cat()

    def get_food(self):
        ''' returns cat food object '''

        return "Cat food!"

class PetStore:

    def __init__(self, pet_factory: PetFactory):

        self._pet_factory = pet_factory

    def show_pet(self):

        pet = self._pet_factory.get_pet()
        
        petFood = self._pet_factory.get_food()

        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("Our pet eats '{}'".format(petFood))


petStore = PetStore(DogFactory())

petStore.show_pet()

petStore._pet_factory = CatFactory()

petStore.show_pet()


