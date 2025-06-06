import logging

logger = logging.getLogger()

def do_something():
    logger.debug("Prepare to do something")
    logger.debug("Doing something")
    logger.warning("Done do something")

def main():
    logging.basicConfig(level=logging.INFO)
    logger.warning("Hello! Starting main")
    do_something()
    logger.warning("Done doing something")

if __name__ == "__main__":
    main()


