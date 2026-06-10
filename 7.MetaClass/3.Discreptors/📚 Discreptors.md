
---

# 📚 Python Descriptors: Core Concepts & Implementation

Python descriptors are a powerful protocol that allows you to customize attribute access (getting, setting, and deleting). This note covers the implementation patterns found in your code.

## 🔹 1. Descriptor Protocol Overview

A descriptor is simply an object that implements at least one of these methods:

- `__get__(self, instance, owner)`: Triggered when accessing an attribute.
    
- `__set__(self, instance, value)`: Triggered when assigning a value.
    
- `__set_name__(self, owner, name)`: Triggered at class creation to capture the attribute name.
    

---

## 🔹 2. Data Descriptors (Validation & Tracking)

Data descriptors implement `__set__`. They are ideal for validating data or logging changes.

### A. The `PositiveNumber` Validator

[positive_number.py](...7.MetaClass/6.parctice/descriptors/positive_number.py)



This descriptor ensures that numeric dimensions (like radius or width) are strictly greater than zero.

Python

``` python
# descriptors/positive_number.py
from typing import TypeVar

T = TypeVar("T")

class PositiveNumber:
    def __set_name__(self, owner, name):
        # Captures the name of the attribute, e.g., 'radius'
        self.attr_name = f"_{name}"

    def __get__(self, instance, owner) -> T:
        # Returns the private attribute value
        return getattr(instance, self.attr_name)

    def __set__(self, instance, value: T) -> None:
        # Enforces the positive-only rule
        if value <= 0:
            raise ValueError(f"Value must be positive, got {value}")
        setattr(instance, self.attr_name, value)
```

### B. The `NoisyDescriptor` (Logging)

Used to track when attributes are modified or accessed in the system.

Python

``` python
class NoisyDescriptor:
    def __set_name__(self, owner, name):
        print(f'Received {name=} of type {owner=}')
        self.private_name = f'_{name}'

    def __get__(self, obj, objcls):
        print(f'Getting {self.private_name} from {obj=}')
        return getattr(obj, self.private_name, "Nothing here !!!")

    def __set__(self, obj, value):
        print(f"Setting {value=} on {obj=}")
        setattr(obj, self.private_name, value)
```

---

## 🔹 3. Constant & Read-Only Descriptors

You can use descriptors to create immutable attributes or strict constants.

Python

``` python
class Constant:
    def __init__(self, value, strict=False):
        self.value = value
        self.strict = strict

    def __get__(self, obj, objels):
        return self.value

    def __set__(self, obj, value):
        if self.strict:
            raise AttributeError("Can't change a constant value")
```

---

## 🔹 4. Non-Data Descriptors

Non-data descriptors only implement `__get__`. These are commonly used for methods or static properties.

Python

``` python
class Yes:
    """A non-data descriptor that just returns 'yes'"""
    def __get__(self, instance, owner):
        return "yes"
```

---

## 🛠 Usage Example in Domain Logic

In your project, these descriptors are applied within the shape classes to maintain clean code and separate validation logic from geometry logic.

Python

``` python
# shapes/circle.py
class Circle(Shape):
    radius = PositiveNumber()  # Using the descriptor

    def __init__(self, radius: float) -> None:
        self.radius = radius  # Triggers PositiveNumber.__set__

    @property
    def area(self) -> float:
        return math.pi * self.radius**2
```

---

## 🚀 Summary Table

|**Method**|**Purpose**|**Implementation Context**|
|---|---|---|
|`__set_name__`|Captures variable name|`PositiveNumber`, `NoisyDescriptor`|
|`__get__`|Logic for retrieving value|`Constant`, `Yes`, `Validator`|
|`__set__`|Logic for setting/validating|`PositiveNumber`, `Number`, `LowerStr`|

#Python #OOP #Descriptors #CleanCode #ProgrammingPractice
[[...7.MetaClass/6.parctice/descriptors/positive_number.py]]
[[common.py]]
[[descriptors.py]]
[[main.py]]
[[practice.py]]
[[test.sql]]
