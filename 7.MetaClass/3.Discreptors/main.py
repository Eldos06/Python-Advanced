from common import  configure_logging
import logging
configure_logging()

# удобная функция, как print()
def log(message, *args, level=logging.INFO, **kwargs):
    logging.log(level, str(message), *args, **kwargs)

class User:
    name = "Sam"
user = User()
log(user)
# log("Hello world")        # как print()
# log(User.name)            # выведет имя
# log("Something bad", level=40)  # WARNING/ERROR можно через level
# log(User.__dict__)  # выведет словарь атрибутов
log(user.__dict__)
log(user.name)

log(type.__getattribute__(User, 'name'))
log(type.__getattribute__(User, '__dict__'))


log(object.__getattribute__(user, 'name'))

