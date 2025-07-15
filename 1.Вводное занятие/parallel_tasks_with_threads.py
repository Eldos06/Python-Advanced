from time import sleep

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
    thread_users = Thread(target=get_users)
    thread_posts = Thread(target=get_posts)
    logger.info("create demo treading")
    thread_users.start()
    thread_posts.start()
    logger.info("started threads, joining")
    thread_users.join()
    thread_posts.join()

    logger.info("done demo treading")

def main():
    configure_logging()
    logger.info("start main")
    demo_threading()
    logger.info("done main")

if __name__ == '__main__':
    main()