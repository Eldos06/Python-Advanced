# class Animal:
#     def __init__(self, name):
#         self.name = name  # 'self' refers to the current instance

#     def speak(self):
#         print(f"{self.name} makes a sound.")

# class Dog(Animal):
#     def __init__(self, name, breed):
#         self.name = name  # Accessing the attribute with 'self'
#         self.breed = breed  # Accessing the attribute with 'self'

#     def speak(self):
#         self.name = "Updated Name"  # Changing the name using 'self'
#         print(f"{self.name} barks!")

# dog = Dog("Rex", "Golden Retriever")
# dog.speak()



class Animal:
    def __init__(self, name):
        self.name = name  # 'self' refers to the current instance

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Accessing the attribute with 'self'
        self.breed = breed  # Accessing the attribute with 'self'

    def speak(self):
        super().speak() # Changing the name using 'self'
        print(f"{self.name} barks!")

dog = Dog("Rex", "Golden Retriever")
dog.speak()
