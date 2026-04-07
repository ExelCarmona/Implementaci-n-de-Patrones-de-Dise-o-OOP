from abc import ABC, abstractmethod

# Component Interface
class Coffee(ABC):
    @abstractmethod
    def get_cost(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def get_description(self) -> str:
        raise NotImplementedError

# Concrete Component
class SimpleCoffee(Coffee):
    def get_cost(self) -> float:
        return 2.0

    def get_description(self) -> str:
        return "Café simple"

# Base Decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def get_cost(self) -> float:
        return self._coffee.get_cost()

    def get_description(self) -> str:
        return self._coffee.get_description()

# Concrete Decorators using super() correctly
class MilkDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return super().get_cost() + 0.5

    def get_description(self) -> str:
        return super().get_description() + ", con Leche"

class VanillaDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return super().get_cost() + 0.7

    def get_description(self) -> str:
        return super().get_description() + ", con Vainilla"

if __name__ == "__main__":
    print("Demostración de Decorator:")
    cafe = SimpleCoffee()
    print(f"{cafe.get_description()}: ${cafe.get_cost()} USD")

    cafe_con_leche = MilkDecorator(cafe)
    print(f"{cafe_con_leche.get_description()}: ${cafe_con_leche.get_cost()} USD")
    
    cafe_con_leche_vainilla = VanillaDecorator(cafe_con_leche)
    print(f"{cafe_con_leche_vainilla.get_description()}: ${cafe_con_leche_vainilla.get_cost():.2f} USD")
