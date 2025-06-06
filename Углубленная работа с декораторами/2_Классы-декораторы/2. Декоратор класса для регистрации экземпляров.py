# Напиши декоратор track_instances, который будет хранить все экземпляры классов, которых он декорирует, в списке instances внутри класса.

# Контекст:

# Для каждого класса, который будет украшен этим декоратором, тебе нужно хранить все его экземпляры в атрибуте instances.

# Каждый новый объект, созданный классом, должен добавляться в этот список.
instances = {}

def track_instances(cls):
    cls.__models_registry__ = instances  # Добавляем реестр к самому классу
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)  # Создаем экземпляр
        instances[cls.__name__] = instances.get(cls.__name__, []) + [instance]  # Добавляем экземпляр в реестр
        return instance
    return wrapper

@track_instances
class Person:
    pass

@track_instances
class Boy:
    pass

# Создаем экземпляры классов
person1 = Person()
boy1 = Boy()

# Печатаем реестр экземпляров
print(instances)
