from abc import ABC, abstractmethod

# Product interface
class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        ...

# Concrete Products
class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"

# Creator (Factory Method definition)
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        ...

    def perform_action(self):
        animal = self.create_animal()
        return animal.speak()

# Concrete Creators
class DogFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Cat()

if __name__ == "__main__":
    print("Demostración de Factory Method:")
    
    # We rely on Concrete Creators to spawn the proper instances
    dog_factory = DogFactory()
    cat_factory = CatFactory()
    
    perro = dog_factory.create_animal()
    gato = cat_factory.create_animal()
    
    print(f"El perro dice: {perro.speak()}")
    print(f"El gato dice: {gato.speak()}")
