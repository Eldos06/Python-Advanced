


# Practice: Shapes Meta & Descriptors

## 📌 Project Overview

This project demonstrates a robust Pythonic hierarchy for geometric shapes using **[[Meta classes]]** for automatic class registration and **[[📚 Discreptors]]** for data validation.

### Key Objectives

- **Metaprogramming**: Use a [[Meta classes]] (`ShapeMeta`) to maintain a global registry of all created shape classes.
    
- **Data Integrity**: Implement a descriptor (`PositiveNumber`) to enforce that dimensions like radius, width, and height are strictly positive.
    
- **Abstraction**: Utilize Abstract Base Classes  (via `ABCMeta`) to define a mandatory interface for `area` and `perimeter`. [[ABC & Protocols]]
    

---

## 🛠 Project Structure

The project follows a modular package structure to separate concerns between validation logic and domain models:

Plaintext

```
6.practice/
├── descriptors/
│   ├── __init__.py
│   └── positive_number.py  # Validation logic
├── shapes/
│   ├── __init__.py         # Package exports
│   ├── base.py             # Abstract base class
│   ├── circle.py           # Circle implementation
│   ├── rectangle.py        # Rectangle implementation
│   └── shape_meta.py       # Registration logic
└── main.py                 # Entry point & Demo
```

---

## 💻 Implementation Details

### 1. Data Validation (Descriptor) 

The `PositiveNumber` descriptor uses the `__set_name__` hook to automatically manage attribute names and `__set__` to enforce the positive-only constraint.


[positive_number.py](../descriptors/positive_number.py)

``` python
# descriptors/positive_number.py
from typing import TypeVar

T = TypeVar("T")

class PositiveNumber:
    def __set_name__(self, owner, name):
        # Automatically sets the internal attribute name (e.g., _radius)
        self.attr_name = f"_{name}"

    def __get__(self, instance, owner) -> T:
        return getattr(instance, self.attr_name)

    def __set__(self, instance, value: T) -> None:
        if value <= 0:
            raise ValueError(f"Value must be positive, got {value}")
        setattr(instance, self.attr_name, value)
```

### 2. Automatic Registration (Metaclass)

The `ShapeMeta` metaclass inherits from `ABCMeta`. Every time a new class is defined using this metaclass, it is automatically added to the `shapes` dictionary.

[[../shapes/shape_meta.py]]

``` python
# shapes/shape_meta.py
from abc import ABCMeta

class ShapeMeta(ABCMeta):
    shapes = {}

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        if name in cls.shapes:
            raise ValueError(f"Duplicate shape {name!r}!")
        cls.shapes[name] = cls
```

### 3. Abstract Base Class

The `Shape` class defines the contract for all child shapes using the `@abstractmethod` decorator turned into a property.

[[../shapes/base.py]]

``` python
# shapes/base.py
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
```

---

## 🚀 Key Takeaways

- **Encapsulation**: Descriptors allow us to move validation logic out of `__init__` methods, keeping the shape classes clean.
    
- **Registry Pattern**: By using a metaclass, we don't need to manually keep track of new shapes; they register themselves upon definition.
    
- **Polymorphism**: The `main.py` script demonstrates that we can treat any object inheriting from `Shape` the same way, calling `.area` and `.perimeter` reliably.
    

#Python #Metaprogramming #OOP #DesignPatterns #CodingPractice

[[[../descriptors/__init__.py]]
[[../descriptors/positive_number.py]]

[[../shapes/__init__.py]]
[[../shapes/base.py]]
[[../shapes/circle.py]]
[[../shapes/rectangle.py]]
[[../shapes/shape_meta.py]]

[[../6.parctice.md]]
[[../main.py]]
