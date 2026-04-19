from abc import ABC, abstractmethod

class PositiveNumber:
    def __set_name__(self, owner, name):
        self.attr_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.attr_name)

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Value must be positive")
        setattr(instance, self.attr_name, value)



class Shape(ABC):
    width = PositiveNumber()
    height = PositiveNumber()

    def __init__(self, width, height):
        self.width = width     # вызывает __set__
        self.height = height

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass















