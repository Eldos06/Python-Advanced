from time import sleep
from threading import Thread
from common import configure_logging, timer
from concurrent.futures import Executor, ThreadPoolExecutor
import logging
import requests

logger = logging.getLogger(__name__)


def get_users():
    logger.info("Start get users")
    sleep(1)
    logger.info("Done get users")

def get_posts():
    logger.info("Start get posts")
    sleep(1)
    logger.info("Done get posts")

def get_user(user_id):
    logger.info("get user %s", user_id)
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}",
    )
    result = response.json()
    logger.info("got user %s", result)
    return result



@timer
def demo_threading():
    # with ThreadPoolExecutor() as executor:
    for user_id in range(1, 11):
         get_user(user_id)
    
    logger.info("demo threading done !!!")

def main():
    configure_logging()
    logger.info("start main")
    demo_threading()
    logger.info("done main")

if __name__ == '__main__':
    main()
