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

user = User()
print(user.foo)  # Output: baz
print(User.__bases__)  # Output: (<class '__main__.UserBase'>,)
print(User.mro())


user = type("User", (UserBase,), {"foo": "baz"})
print(user.foo)  # Output: baz
print(user.joo)