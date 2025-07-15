#Многопоточная загрузка пользователей с логированием и таймером

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

def cpu_expensive(time_out):
    logger.info("countdown to %s", time_out)
    while time_out:
        time_out -= 1
    logger.info("done countdown")


@timer
def demo_threading():
    with ThreadPoolExecutor() as executor:
        executor.submit(cpu_expensive, 64_000_000)
        executor.submit(cpu_expensive, 72_000_000)

    # cpu_expensive(64_000_000)
    # cpu_expensive(72_000_000)
    
    logger.info("demo threading done !!!")



def main():
    configure_logging()
    logger.info("start main")
    demo_threading()
    logger.info("done main")

if __name__ == '__main__':
    main()
