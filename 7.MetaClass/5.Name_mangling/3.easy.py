# The Hidden Balance: Create a class Bank with a private attribute __balance.
# Initialize it in the __init__ method.
# Try to print the balance directly from an object instance and observe the AttributeError.
# Then, use vars() to find the "mangled" name and print it.

class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  #private

yeldos = Bank("Yeldos", 90_000_000)

print(yeldos.name)                #Yeldos
# print(yeldos.balance)           #AttributeError: 'Bank' object has no attribute 'balance'
# print(yeldos.__balance)         #AttributeError: 'Bank' object has no attribute '__balance'
# print(vars(yeldos))             #{'name': 'Yeldos', '_Bank__balance': 90000000}
print(yeldos.__dict__)            #{'name': 'Yeldos', '_Bank__balance': 90000000}
print(yeldos.__class__)           #<class '__main__.Bank'>
yeldos._Bank__balance = 90
# print(yeldos.__dict__)          #{'name': 'Yeldos', '_Bank__balance': 90}



class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value

    def info(self):
        return f"User name: {self.name}\nBalance: {self.balance}"

user = Bank("Dossymzhan", 90_000_000)

print(user.info())

user.balance = 90   # через setter
print(user.info())












