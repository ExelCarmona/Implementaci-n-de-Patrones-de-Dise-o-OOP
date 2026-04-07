from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def get_animal(animal_type: str) -> Animal:
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        raise ValueError("Tipo de animal desconocido")

if __name__ == "__main__":
    print("Demostración de Factory Method:")
    factory = AnimalFactory()
    
    perro = factory.get_animal("dog")
    gato = factory.get_animal("cat")
    
    print(f"El perro dice: {perro.speak()}")
    print(f"El gato dice: {gato.speak()}")
