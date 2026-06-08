from descriptors.positive_number import PositiveNumber
from shapes.base import Shape


class Rectangle(Shape):
    width = PositiveNumber()
    height = PositiveNumber()

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}(width={self.width!r}, height={self.height!r})"
        )

    def __repr__(self) -> str:
        return str(self)