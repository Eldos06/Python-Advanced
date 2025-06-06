 
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} cannot speak"

class Dog(Animal):
    def __init__(self, name, age,breed):
        super().__init__(name)
        self.breed = breed
        self.age = age


    def showInfo(self):
        return f"name: {self.name} breed: {self.breed}  age: {self.breed}"

    
tuz = Dog("Tuzik", 32, "Mashky")
print(tuz.showInfo())