import math

from descriptors.positive_number import PositiveNumber
from shapes.base import Shape


class Circle(Shape):
    radius = PositiveNumber()

    def __init__(self, radius: float) -> None:
        self.radius = radius

    @property
    def area(self) -> float:
        return math.pi * self.radius**2

    @property
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    @property
    def circumference(self) -> float:
        return self.perimeter

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(radius={self.radius!r})"

    def __repr__(self) -> str:
        return str(self)