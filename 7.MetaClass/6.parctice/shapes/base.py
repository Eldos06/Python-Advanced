from abc import abstractmethod

from shapes.shape_meta import ShapeMeta


class Shape(metaclass=ShapeMeta):
    @property
    @abstractmethod
    def area(self) -> float:
        raise NotImplementedError

    @property
    @abstractmethod
    def perimeter(self) -> float:
        raise NotImplementedError