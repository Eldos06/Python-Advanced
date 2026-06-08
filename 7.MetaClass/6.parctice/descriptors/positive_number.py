from typing import TypeVar

T = TypeVar("T")


class PositiveNumber:
    def __set_name__(self, owner, name):
        self.attr_name = f"_{name}"

    def __get__(self, instance, owner) -> T:
        return getattr(instance, self.attr_name)

    def __set__(self, instance, value: T) -> None:
        if value <= 0:
            raise ValueError(f"Value must be positive, got {value}")
        setattr(instance, self.attr_name, value)