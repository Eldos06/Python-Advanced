[[Meta classes]]
[[main.py]]
[[practice.py]]
## 1. Standard Classes vs. Memory Usage

By default, Python objects use a dictionary (`__dict__`) to store instance attributes. This allows for dynamic attribute assignment but consumes a significant amount of memory.

- **Dynamic Assignment:** You can add new attributes to an instance at any time (e.g., `user1.email = '...'`).
    
- **Memory Overhead:** Storing a dictionary for every single object instance is "heavy," especially when creating thousands of objects.

```python
from sys import getsizeof

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user1 = User('John', 36)
user1.email = '321452@sdu.edu.kz' # Dynamically added
print(getsizeof(user1))           # Larger memory footprint
```


## 2. Using `__slots__` for Efficiency

The `__slots__` declaration allows you to explicitly define which attributes a class can have.

- **Memory Savings:** Python reserves space for only the specified attributes and does **not** create a `__dict__` for each instance.
    
- **Restriction:** You cannot add new attributes that are not defined in `__slots__`. Attempting to do so will raise an `AttributeError`.
    
- **Attribute Deletion:** You can still delete attributes defined in slots using `del`.

```python
class User:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age

user1 = User('John', 36)
# user1.email = '...' # This would crash: AttributeError
del user1.name        # Attribute can be removed
print(user1.age)
print(user1.name)
```


## 3. Data Classes with Slots

The `@dataclass` decorator (introduced in Python 3.7) simplifies class creation. In more recent versions, you can enable `slots` directly within the decorator.

- **`slots=True`:** Automatically generates `__slots__` based on the type hints provided in the class, combining the convenience of dataclasses with the memory efficiency of slots.

```python
from dataclasses import dataclass

@dataclass(slots=True)
class User:
    username: str
    age: int

print(User.__slots__) # Output: ('username', 'age')
```


## 4. Immutable Data Classes (`frozen=True`)

To create a "Read-Only" object where attributes cannot be modified after the object is created, use the `frozen` parameter.

- **`frozen=True`:** Makes the instance immutable. Any attempt to change an attribute (e.g., `yeldos.name = 'Yerbol'`) will raise a `FrozenInstanceError`.
    
- **Data Integrity:** This is excellent for ensuring that data remains constant throughout the program's lifecycle.

```python
@dataclass(slots=True, frozen=True)
class User:
    username: str
    age: int

yeldos = User('Yeldos', 36)
# yeldos.username = 'Yerbol' # Raises FrozenInstanceError
```


| Feature            | Standard Class     | `__slots__ `Class   | Frozen Dataclass    |
| ------------------ | ------------------ | ------------------- | ------------------- |
| Storage            | `__dict__` (Heavy) | Fixed Array (Light) | Fixed Array (Light) |
| Dynamic Attributes | Yes                | No                  | No                  |
| Mutable            | Yes                | Yes                 | No                  |
| Boilerplate        | Medium             | Medium              | Low                 |

