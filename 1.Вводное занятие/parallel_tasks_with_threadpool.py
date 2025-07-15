from time import sleep
from concurrent.futures import ThreadPoolExecutor 
import logging
from threading import Thread
from common import configure_logging, timer

logger = logging.getLogger(__name__)


def get_users():
    logger.info("Start get users")
    sleep(1)
    logger.info("Done get users")

def get_posts():
    logger.info("Start get posts")
    sleep(1)
    logger.info("Done get posts")


@timer
def demo_threading():
    with ThreadPoolExecutor() as executor:
        executor.submit(get_users)
        executor.submit(get_posts)

def main():
    configure_logging()
    logger.info("start main")
    demo_threading()
    logger.info("done main")

if __name__ == '__main__':
    main()