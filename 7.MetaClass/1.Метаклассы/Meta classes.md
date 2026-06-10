
## 1. Classes vs. Types

In Python, classes are objects too. Everything, including the `class` definition itself, is an instance of `type`.

- **`__class__` vs `type()`**: These are generally identical; they return the type of the object.
    
- **The `type` class**: This is a "metaclass." All classes (`int`, `dict`, `User`) are instances of `type`.

```python
class User:
    pass

user = User()
print(type(user))  # <class 'User'>
print(type(User))  # <class 'type'> - The class itself is an instance of 'type'
```


## 2. Dynamic Class Creation

You don't always need the `class` keyword. You can create classes dynamically using the `type()` constructor:

`type(name, bases, dict)`

|**Parameter**|**Purpose**|
|---|---|
|**Name**|A string defining the class name.|
|**Bases**|A tuple of parent classes (inheritance).|
|**Dict**|A dictionary containing attributes and methods.|
```python
# Creating a class dynamically
User = type("User", (), {"first_name": "Suleimen", "last_name": "Yeldos"})

user = User()
print(user.first_name) # Suleimen


```


## 3. The `__new__` Method

While `__init__` initializes an instance, `__new__` is the method that actually **creates** the instance.

- **Usage**: It is primarily used when inheriting from immutable types (like `tuple` or `str`) or in design patterns like Singletons.
    
- **Return Value**: It must return a new instance of the class.

```python
class UsernamesTuple(tuple):
    def __new__(self, iterable):
        # Transforming data BEFORE the object is even created
        lower_str = (s.lower() for s in iterable)
        return super().__new__(self, lower_str)

r = UsernamesTuple(["Suleimen", "Yeldos"])
print(r) # ('suleimen', 'yeldos') - All lowercased
```

## 4. Metaclasses (`metaclass=...`)

A Metaclass is a "class for a class." It allows you to intercept the creation of a class to modify its attributes automatically.

### Example: CamelCase to snake_case

You can create a metaclass that automatically renames all class attributes to follow `snake_case` conventions.

```python
class CamelToSnakeMeta(type):
    def __new__(cls, name, bases, attrs):
        snake_attrs = {}
        for attr_name, attr_value in attrs.items():
            # (Logic to convert CamelCase to snake_case)
            snake_name = camel_to_snake(attr_name) 
            snake_attrs[snake_name] = attr_value
        return super().__new__(cls, name, bases, snake_attrs)

class User(metaclass=CamelToSnakeMeta):
    userName = "Yeldos" # This will be transformed to user_name

user = User()
print(user.user_name) # Output: Yeldos
```

## 5. `__init_subclass__`

Introduced in Python 3.6, this is a simpler alternative to metaclasses. It is called whenever a class is inherited.

- **Benefit**: It allows parent classes to configure child classes without the complexity of a full metaclass.

```python
class Node:
    def __init_subclass__(cls, node_pos):
        cls.pos = node_pos

class LeftNode(Node, node_pos="left"):
    pass

print(LeftNode.pos) # Output: left
```

### Summary Table: Class Modification Tools

| **Feature**         | **When to use?**                                                       | **Complexity** |
| ------------------- | ---------------------------------------------------------------------- | -------------- |
| `__init__`          | To set initial values on a new object.                                 | Low            |
| `__new__`           | To control the creation of immutable objects or custom instance types. | Medium         |
| `__init_subclass__` | To set attributes on subclasses automatically.                         | Medium         |
| #metaclass          | To change how the class itself is built (global changes).              | High           |
[[main.py]]
[[tasks.py]]
