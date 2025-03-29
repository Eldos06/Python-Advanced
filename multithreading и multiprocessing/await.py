from time import sleep

import logging

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
    get_users()
    get_posts()

def main():
    configure_logging()
    logger.info("start main")
    demo_threading()
    logger.info("done main")

if __name__ == '__main__':
    main()