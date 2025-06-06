from time import sleep
import logging
from random import randint
logger = logging.getLogger(__name__)

class User:

    def __str__(self):
        sleep(0.9)
        return f"{self.__class__.__name__}(id={id(self)})"

def something_expensive():
    sleep(5)
    logger.warning("Done something expensive")
    return [{"message": "something expensive"}]


def do_something():
    number = randint(a=1, b=100)
    user = User()
    word = "query"

    logger.debug(
        "Prepare to do something, number: %s, word: %r, user: %s",
        number,
        word,
        user
                )
    
    logger.info(
        "Doing something number: %s, user: %s",
        number,
        user
                )
    logger.warning("Expensive message: %s", something_expensive())
    
    logger.warning("Done do something")