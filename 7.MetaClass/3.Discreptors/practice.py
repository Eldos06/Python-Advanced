from abc import ABC, abstractmethod
from respect_validation import Validator as v

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    @property
    def full_name(self):

      return f"{self.first_name} {self.last_name}"




# # Example usage:
# person = Person("Alex", "Kim")
# print(person.full_name) # Should print "Alex Kim"

# Use the 'Number' class from the lecture
# ...


# ==== Валидатор числа ====
# class Number(Validator):
#     def __init__(self, min_value=1, max_value=None):
#         self.min_value = min_value
#         self.max_value = max_value

#     def validate(self, value):
#         if not isinstance(value, int):
#             raise TypeError(f"Value {value} has to be type {int}, not {type(value)}")
#         value = int(value)

#         if value < self.min_value:
#             raise ValueError(f"Value {value} is less than {self.min_value}")


#         return value
####################################################################################




# Task 3: Simple File Path Descriptor
# Create a simple descriptor LogFile that always returns the same file path. This is a "non-data descriptor" because it only has a __get__ method.

# Goal: Accessing Config.log_path should always return "/var/log/app.log".

# Python

# class LogFile:
#     def __get__(self, instance, owner):
#         # Your code here
#         # Return the string "/var/log/app.log"
#         return "/var/log/app.log"

# class Config:
#     log_path = LogFile()

# # Example usage:
# config = Config()
# print(config.log_path) # Should print /var/log/app.log
# print(Config.log_path) # Should also print /var/log/app.log








# Medium Tasks (Level 4-6)
# These tasks are more complex and require you to build new validators.

# Task 4: String Length Validator
# Create a new validator StringWithLength that inherits from the Validator base class. It should check two things:

# The value is a str.

# The string's length is between min_length and max_length.

# Goal: The username must be a string between 3 and 10 characters long.

# Python

# Use the 'Validator' class from the

# # ==== Абстрактный валидатор ====
# class Validator(ABC):
#     def __set_name__(self, owner, name):
#         self.attr_name = '_' + name

#     def __get__(self, instance, owner):
#         print('get attr', self.attr_name)
#         return getattr(instance, self.attr_name) # getattr is used to get the value of an attribute from an object

#     def __set__(self, instance, value):
#         print('validate', repr(value), 'before setting to', self.attr_name)
#         value = self.validate(value)
#         print('set', repr(value), 'to attr', self.attr_name)
#         setattr(instance, self.attr_name, value)

#     @abstractmethod
#     def validate(self, value):
#         pass



# # ==== Валидатор строки ====
# class LowerStr(Validator):
#     def validate(self, value):
#         if not isinstance(value, str):
#             raise TypeError(f'Value {value} has to be type {str}, not {type(value)}')
#         return value.lower()
# # ...

# class StringWithLength(Validator):
#     def __init__(self, min_length=None, max_length=None):
#         # Save min_length and max_length
#         pass

#     def validate(self, value):
#         # Check if value is a string
#         # Check if length is correct
#         # Return the value if it's okay
#         pass

# class UserProfile:
#     username = StringWithLength(min_length=3, max_length=10)

#     def __init__(self, username):
#         self.username = username

# # Example usage:
# profile_ok = UserProfile("testuser")
# print(profile_ok.username)

# try:
#     profile_fail = UserProfile("no") # Too short, should fail
# except ValueError as e:
#     print(e)


# #Write-Once Descriptor
# Create a descriptor that allows you to set a value only one time. If you try to change the value again, it should raise an AttributeError. This is useful for configuration settings that should not change.

# Goal: You can set config.api_key once. A second try must fail.

class WriteOnce:
    count = 0
    def __set_name__(self, owner, name):
        self.attr_name = '_' + name #self.attr_name is the name of the attribute with a leading underscore

    def __get__(self, instance, owner):
        return getattr(instance, self.attr_name)

    def __set__(self, instance, value):
        # Check if the attribute already exists on the instance
        # If it exists, raise an error



        # If not, set the attribute
        pass

class AppConfig:
    api_key = WriteOnce()

# Example usage:
config = AppConfig()
config.api_key = "secret-key-123" # This should work
print(config.api_key)

try:
    config.api_key = "new-key-456" # This should raise an AttributeError
except AttributeError as e:
    print(e)


