from abc import ABCMeta


# class ShapeMeta(type):
class ShapeMeta(ABCMeta):
    shapes = {}

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        if name in cls.shapes:
            raise ValueError(f"Duplicate shape {name!r}!")
        cls.shapes[name] = cls