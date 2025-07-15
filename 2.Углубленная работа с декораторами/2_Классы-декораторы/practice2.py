def add_prefix(prefix):
    def class_decorator(class_to_decorate):
        class DecoratedClass(class_to_decorate):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.prefix = prefix
 
            def get_prefixed_name(self):
                return self.prefix + self.name
        return DecoratedClass
    return class_decorator
 
@add_prefix("Mr. ")
class Person:
    def __init__(self, name):
        self.name = name
 
person = Person("John")
print(person.get_prefixed_name())  # вывод: Mr. John


