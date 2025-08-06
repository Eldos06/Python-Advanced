# class User:
#   pass

# user = User()
# print(user)
# print(user.__class__) # <class '__main__.User'>
# print(type(user)) # <class '__main__.User'>

# print(user.__class__ is type(user)) # True

# data = {'Suleimen': "Yeldos"}
# print(data)
# print(data.__class__) # <class 'dict'>
# print(type(data)) # <class 'dict'>

# print()

# print(User)
# print(type(dict)) #<class 'type'>
# print(type(int)) # <class 'type'>
# print(type(dict) is type) # <class 'type'>

# print()
# print(type(type))

# print(help(type)) # Help on class type in module builtins:


User = type("User", (), {})

user = User()
# print(user)

class UserBase:
  foo = "bar"

class User(UserBase):
  foo = "baz"

# user = User()
# print(user.foo)  # Output: baz
# print(User.__bases__)  # Output: (<class '__main__.UserBase'>,)
# print(User.mro())


# user = type("User", (UserBase,), {"foo": "baz"})
# print(user.foo)  # Output: baz
# print(user.joo)


class User():
  first_name = ""
  last_name = ""

  def get_full_name(self):
    return f"{self.first_name} {self.last_name}".strip()


# user = User()
# user.first_name = " Suleimen"
# user.last_name = " Yeldos "
# # print(user.get_full_name().__repr__())
# print(vars(User))  # Output: {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'User' objects>, '__weakref__': <attribute '__weakref__' of 'User' objects>, '__doc__': None, 'first_name': '', 'last_name': '', 'get_full_name': <function User.get_full_name at 0x000001C3B8F5FCA0>}


User = type(
  "User",
  (),
  {
    "first_name": "",
    "last_name": "",
    "get_full_name": User.get_full_name,  # Reference the method from the User class
  }
)





# user = User()
# user.first_name = " Suleimen"
# user.last_name = " Yeldos "
# # print(user.get_full_name().__repr__())
# print(vars(User))  # Output: {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'User' objects>, '__weakref__': <attribute '__weakref__' of 'User' objects>, '__doc__': None, 'first_name': '', 'last_name': '', 'get_full_name': <function User.get_full_name at 0x000001C3B8F5FCA0>}


class User:
  # This is the class definition for User
  def __new__(cls): # This method is called to create a new instance of the class
    u = super().__new__(cls) # Call the parent class's __new__ method to create a new instance
    u.first_name = ""
    u.last_name = ""
    return u  # Return the new instance
user = User()


# print(vars(User))

# print(vars(user))  # Output: {'first_name': '', 'last_name': ''}


# class Parent:
#   attr = "parent"

# class Child:
#   attr = "child"

# class Family:
#   _members = []
#   def __new__(cls, other_class):
#     instance = super().__new__(other_class)
#     cls._members.append(instance)
#     return instance

# child = Family(Child)
# print(child.attr)  # Output: child
# print(child)

# print(Family._members)  # Output: [<__main__.Child object at 0x...>]
# print(type(child))  # Output: <class '__main__.Child'>
# print(type(Family))

# parent = Family(Parent)

# print(parent.attr)  # Output: parent
# print(parent)
# print(Family._members)  # Output: [<__main__.Child object at 0x...>, <__main__.Parent object at 0x...>]
# print(type(parent))  # Output: <class '__main__.Parent'>

class Meta(type):
  def __init__(cls, name, *args, **kwargs):
    cls.spam = "eggs"  # Add an attribute to the class

class Base:
  spam = "eggs"

class A(Base):
  pass

class B(Base):
  pass

A.spam = "eggs eggs"  # Modify the class attribute for A
B.spam = "eggs eggs"  # Modify the class attribute for B

# print(A.spam)  # Output: eggs eggs
# print(B.spam)  # Output: eggs eggs

# print(A.mro())  # Output: [<class '__main__.A'>, <class '__main__.Meta'>, <class 'object'>]
# print(type(A))  # Output: <class '__main__.Meta'>

# class UsernamesTuple(tuple):
#   def __init__(self, itearable):
#     print("init cls w/", itearable)
#     print("self", self)

# r = UsernamesTuple(["suleimen", "yeldos", "suleimen_yeldos"])
# print(r)  # Output: UsernamesTuple(['suleimen', 'yeldos',

class UsernamesTuple(tuple):
  def __new__(self, itearable):
    lowerStr = (s.lower() for s in itearable)
    return super().__new__(self, lowerStr)

r = UsernamesTuple(["Suleimen", "Yeldos", "Suleimen_yeldos"])
# print(r)  # Output: UsernamesTuple(['suleimen', 'yeldos', 'suleimen_yeldos'])
# print(type(r))  # Output: <class '__main__.UsernamesTuple'>

def camel_to_snake(name):
  snake_name_chars = []
  for i, char in enumerate(name):
    if char.isupper() and i > 0:
      snake_name_chars.append('_')
    snake_name_chars.append(char.lower())
  return ''.join(snake_name_chars)
class CamelToSnakeMeta(type):
  def __new__(cls, name, bases, attrs):
    snake_attrs = {}
    for attr_name, attr_value in attrs.items():
      snake_name = camel_to_snake(attr_name)
      snake_attrs[snake_name] = attr_value
    return super().__new__(cls, name, bases, snake_attrs)

class User(metaclass=CamelToSnakeMeta):
  userName = "Yeldos2"
  age = 20

  def increse_age(self):
    self.age += 1
    return self.age


user = User()
print(user.user_name)  # Output: Yeldos2
print(user.age)
user.increse_age()
print()








