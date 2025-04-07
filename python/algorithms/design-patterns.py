from abc import ABC, abstractmethod
from typing import Union


# Singleton Pattern
class Singleton:
    """
    - Ensures only one instance of a class exists
    - Used in logging, database connections, and configuration management
    """

    _instance = None

    def __new__(self):
        if self._instance is None:
            self._instance = super().__new__(self)
        return self._instance


# Factory Pattern
class Factory:
    """
    - Creates objects without exposing class names
    - Used when we do not know the exact class type at runtime
    """

    @staticmethod
    def get_type(type):
        types = {"dog": Dog(), "cat": Cat()}
        return types.get(type.lower(), None)


class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"


# Builder Pattern
class Builder:
    """
    - Step-by-step object construction
    - Used when objects have many parameters or complex construction logic
    Example Usage
    building = (Builder().add_building_block("foundation").add_building_block("flooring").build())
    """

    def __init__(self):
        self.blocks = []

    def add_building_block(self, block):
        self.blocks.append(block)
        return self

    def build(self):
        return f"Building with {', '.join(self.blocks)}"


# Observer Pattern
class Observer(ABC):
    """
    - Notify multiple objects when a state changes
    - Used in event-driven programming, UI frameworks, and pub-sub systems
    """

    @abstractmethod
    def update(self, message):
        pass


class User(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received message: {message}")


class Newsletter:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, observer):
        self.subscribers.append(observer)

    def notify(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)


# Strategy Pattern
class PaymentStrategy(ABC):
    """
    - Dynamically change behavior at runtime
    - Used in AI, game development, and algorithm selection
    """

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")


class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} with Bitcoin")


class ShoppingCart:
    def __init__(
        self, payment_strategy: Union[CreditCardPayment, PayPalPayment, BitcoinPayment]
    ):
        self.payment_strategy = payment_strategy

    def checkout(self, amount):
        self.payment_strategy.pay(amount)
