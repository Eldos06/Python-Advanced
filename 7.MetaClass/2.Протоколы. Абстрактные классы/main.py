# # Протоколы. Абстрактные классы
# from time import time
# from abc import ABC, abstractmethod
# class Animal:
#   def get_sound(self):
#     return ""

#   def get_breed(self):
#     return ""

# class Cat(Animal):
#   def __init__(self, name):
#     self.name = name

# cat = Cat("Mura")
# # print(isinstance(cat, Cat))
# # print(Cat.mro())
# # print(issubclass(Cat, Animal))
# # print(cat.get_breed())

# class Animal(ABC):
#   @abstractmethod
#   def get_sound(self):
#     """
#     Animal sound
#     """

#   @abstractmethod
#   def get_breed(self):
#     pass

# # print(Animal.__mro__)
# # class Cat(Animal):
# #   def __init__(self, name, breed):
# #     self.name = name
# #     self.breed = breed



# class Animal(ABC):
#   @abstractmethod
#   def get_sound(self):
#     """
#     Animal sound
#     """
#   @classmethod
#   @abstractmethod
#   def get_breed(self):
#     self

# class OrientalCat(Cat):
#   def get_breed(self):
#     return "Oriential Cat"
#   @classmethod
#   def get_sound(cls):
#     return "Meow"


# cat = OrientalCat("Mura")
# # print()
# # print(cat)
# # print(type(cat))
# # print(cat.name)
# # print(cat.get_breed())
# # print(cat.get_sound())

# # print(OrientalCat.get_sound())
# # print(cat.get_breed())


# class Dog:
#   def __init__(self, name, breed):
#     self.name = name
#     self.breed = breed

#   def get_sound(self):
#     return "woof"

#   def get_breed(self):
#     return self.breed

# # print(issubclass(Dog, Animal))
# # print(Dog.mro())


# class Animal(ABC):
#   @abstractmethod
#   def get_sound(self):
#     """
#     Animal sound
#     """
#   @classmethod
#   @abstractmethod
#   def get_breed(self):
#     self
#   @classmethod
#   def __subclasshook__(cls, other):
#     if cls is Animal and all(hasattr(other, name) for name in ["get_sound", "get_breed"]): # Check if the other class has the required methods
#       return True
#     return NotImplemented # NotImplemented is returned if the other class does not have the required methods


# class emailSender(ABC):

#   @abstractmethod
#   def send_email(self, recipient, mail):
#     pass
# # print(emailSender.mro())

# class SMTPSender(emailSender):
#   def __init__(self, host, port):
#     self.host = host
#     self.port = port

#   def send_email(self, recipient, mail):
#     print('sending email', repr(mail), 'by smtp to ', recipient)


# class FileEmailSender(emailSender):
#   def send_email(self, recipient, mail):
#     print('saving email', repr(mail), 'by file for ', recipient)
#     with open(f'email-{recipient}-{time()}.txt', 'w') as f:
#       f.write(f"TO: {recipient}\n\n")
#       f.write(mail)

# smtpEmailSender = SMTPSender('1.1.1.1', 1050)
# smtpEmailSender.send_email('john@example.com', 'Hello John')
# file_email_sender = FileEmailSender()
# file_email_sender.send_email('john@example.com', 'Hello John')

# class NotificationManager:
#   def __init__(self, email_sender: emailSender):
#     if not isinstance(email_sender, emailSender):
#       raise TypeError(f"email_sender must be an instance of emailSender, we got {type(email_sender)}")
#     self.email_sender = email_sender

#   def send_alert(self, to, subject):
#     print('sending ALERT to', to)
#     alert_message = (
#       f"[ALERT] {subject}\n\n"
#       "Hi\n"
#       "This is an alert message.\n"
#     )
#     self.email_sender.send_email(to, alert_message)

# notification_system = NotificationManager(email_sender= smtpEmailSender)
# print(notification_system.email_sender)
# print(notification_system)
# notification_system.send_alert("john@example.com", "Test Alert")