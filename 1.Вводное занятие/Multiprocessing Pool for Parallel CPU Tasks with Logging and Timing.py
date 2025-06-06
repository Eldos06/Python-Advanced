#Многопоточная загрузка пользователей с логированием и таймером
#Параллельные CPU-задачи с помощью multiprocessing.Pool, логированием и таймером

from time import sleep
from threading import Thread
from common import configure_logging, timer
from concurrent.futures import Executor, ThreadPoolExecutor
import logging
import requests
import multiprocessing

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
def demo_multiproccessing():
    logger.info("start demo multiproccessing")
    # process_1 = multiprocessing.Process(
    #     target=cpu_expensive,
    #     args=(64_000_000,),
    #     )
    # process_2 = multiprocessing.Process(
    #     target=cpu_expensive,
    #     args=(72_000_000,),
    #     )
    # logger.info("created procs, starting")
    # process_1.start()
    # process_2.start()
    # logger.info("started procs, joining")
    # process_1.join()
    # process_2.join()
    # logger.info("done demo multiproccessing")
    
    with multiprocessing.Pool() as pool:
        pool.map(cpu_expensive, [64_000_000, 72_000_000])


def main():
    configure_logging()
    logger.info("start main")
    demo_multiproccessing()
    logger.info("done main")

if __name__ == '__main__':
    main()
