[[Meta classes]]
[[main.py|Main]]

#Protected 
==**Protected Access Modifier**==  
A member is considered protected if its name starts with a single underscore (_).A member is considered protected if its name starts with a single underscore (_).
Convention only: It suggests that the member should not be accessed outside the class except by subclasses.
Still, Python allows direct access if explicitly called.
```python
class User:  
    def __init__(self, name, password):  
        self.name = name  
        self._password = password # Protected - should do not touch (but u can do it)  
  
user = User("John", "Doslend")  
print(user.name)      #John  
print(user._password) #Doslend  
print()
```

#Private
 **==Private Access Modifier==**
A member is private if its name starts with double underscores (__).  
Python does not enforce strict privacy — instead, it uses Name Mangling.  
The interpreter renames __var to _ClassName__var internally.

```python
class User:  
    def __init__(self, name, password):  
        self.name = name  
        self.__password = password # Private - You can not access it outside of class!  
  
user = User("John", "Hehehheh")  
print(user.name)      #John  
# print(user.__password)    #AttributeError: 'User' object has no attribute '__password'  
print(user.__dict__)        # {'name': 'John', '_User__password': 'Hehehheh'}  
print(user.__dict__.keys()) # dict_keys(['name', '_User__password'])  
print(vars(user))           #{'name': 'John', '_User__password': 'Hehehheh'}  
print(user._User__password) # Hehehheh
```


#Hash 

Hashing is a technique that transforms variable-length input (like a string) into a fixed-length output (a "hash" or "digest") to enable fast data retrieva

```python
import hashlib
class User:  
    def __init__(self, name, password):  
        self.name = name  
        self.__password = None   # To instantly hashing new value  
        self.password = password #  
  
    @property  
    def password(self):  
        return self.__password  
  
    @password.setter  
    def password(self, value):  
        self.__password = hashlib.sha256(value.encode()).hexdigest()  
  
    @password.deleter  
    def password(self):  
        self.__password = None  
print()  
user = User("John", "Golofking")  
print(user.name)  
print(user.password)  
user.password = "sdaf"  
print(user.password)  
print(vars(user))  
# print(user.__password)          # AttributeError: 'User' object has no attribute '__password'. Did you mean: 'password'?
```




[[3.easy.py|Easy Example]]

