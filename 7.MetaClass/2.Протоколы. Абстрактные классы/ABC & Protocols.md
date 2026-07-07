[[main.py]]

---

# 📖 Python Interfaces: Abstract Classes vs. Protocols

This note explores two ways to define "contracts" for classes in Python: **Nominal Typing** with `abc.ABC` and **Structural Typing** with `typing.Protocol`.

## 🏛️ 1. Abstract Base Classes (ABC)

Abstract classes are used for **Nominal Typing**. A class must explicitly inherit from the ABC to be considered a subclass.

### Key Implementation (from `main.py`):

Python

``` python
from abc import ABC, abstractmethod

class EmailSender(ABC):
    @abstractmethod
    def send_email(self, recipient, mail):
        """Must be implemented by subclasses"""
        pass

class SMTPSender(EmailSender):  # Explicit inheritance
    def send_email(self, recipient, mail):
        print(f'Sending email via SMTP to {recipient}')
```

- **Enforcement**: Python prevents instantiation of a class if `@abstractmethod` is not overridden.
    
- **Relationship**: It defines an **"is-a"** relationship.
    
- **Subclass Hook**: You can use `__subclasshook__` to allow classes that implement the required methods to be recognized as subclasses without explicit inheritance.
    

---

## 🛠️ 2. Typing Protocols (Duck Typing)

Protocols represent **Structural Typing**. A class is considered a "subclass" simply by having the required methods, even without inheritance.

### Key Implementation (from `base_email_backend.py` and `email_sender.py`):

Python

``` python
from typing import Protocol

class BaseEmailBackend(Protocol):
    def send(self, recipient: str, subject: str, body: str) -> None:
        ...  # Ellipsis used for protocol definitions
```

### Usage in Dependency Injection:

The `EmailSender` class accepts any object that "follows the protocol" of `BaseEmailBackend`.

Python

``` python
class EmailSender:
    def __init__(self, backend: BaseEmailBackend) -> None:
        self.backend = backend  # Accepts anything with a .send() method

    def send(self, recipient: str, subject: str, body: str) -> None:
        self.backend.send(recipient, subject, body)
```

- **Flexible Backends**: Your project implements multiple backends that follow this protocol:
    
    - `loggingEmailBackend`: Outputs to logs.
        
    - `FileEmailBackend`: Saves emails as `.txt` files.
        

---

## ⚖️ Comparison Table

|**Feature**|**Abstract Base Class (ABC)**|**Protocol (Structural)**|
|---|---|---|
|**Inheritance**|Required (Explicit)|Not Required (Implicit)|
|**Type Checking**|Nominal (by name)|Structural (by methods)|
|**Flexibility**|Rigid "Is-A" relationship|Flexible "Acts-Like" relationship|
|**Use Case**|Sharing logic/base behavior|Defining interfaces for external libs|

---

## 🚀 Practical Application: Email System

Your code demonstrates a decoupled email system where the **Sender** logic is separate from the **Transport** (Backend) logic:

1. **Transport Interface**: Defined by `BaseEmailBackend` (Protocol).
    
2. **Specific Transports**: `FileEmailBackend` (saves to disk) and `loggingEmailBackend` (logs to console).
    
3. **Client Logic**: `EmailSender` manages templates and high-level operations, delegating the actual "sending" to the injected backend.
    

#Python #OOP #DesignPatterns #AbstractClasses #Protocols #DependencyInjection

## Файлы проекта `my_package_project/`

[[7.MetaClass/2.Протоколы. Абстрактные классы/my_package_project/email_sender.py|email_sender.py]] - клиентский класс `EmailSender`.
[[7.MetaClass/2.Протоколы. Абстрактные классы/my_package_project/my_package/base_email_backend.py|my_package/base_email_backend.py]] - протокол `BaseEmailBackend`.
[[7.MetaClass/2.Протоколы. Абстрактные классы/my_package_project/my_package/file_email_backend.py|my_package/file_email_backend.py]] - бэкенд, сохраняющий письма в `.txt`-файлы, использует
[[7.MetaClass/2.Протоколы. Абстрактные классы/my_package_project/my_package/hardSubjects.txt|hardSubjects.txt]] как источник тестовых тем писем.
[[7.MetaClass/2.Протоколы. Абстрактные классы/my_package_project/my_package/__init__.py|my_package/__init__.py]] - файл-маркер пакета.
[[7.MetaClass/2.Протоколы. Абстрактные классы/my_package_project/setup.py|setup.py]] - `setup.py` для установки `my_package` как отдельного пакета (`pip install -e .`).
[[7.MetaClass/2.Протоколы. Абстрактные классы/my_package_project/typing.Protocol.py|typing.Protocol.py]] - отдельный черновик/эксперименты с `typing.Protocol` вне основного пакета.