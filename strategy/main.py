from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Pagando ${amount} usando Tarjeta de Crédito.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Pagando ${amount} usando PayPal.")

class ShoppingCart:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def checkout(self, amount: float):
        self._strategy.pay(amount)

if __name__ == "__main__":
    print("Demostración de Strategy:")
    
    carrito1 = ShoppingCart(CreditCardPayment())
    carrito1.checkout(150.00)

    # Cambiamos comportamiento inyectando otra estrategia
    carrito2 = ShoppingCart(PayPalPayment())
    carrito2.checkout(30.50)
