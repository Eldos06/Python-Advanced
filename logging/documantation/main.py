# myapp.py
import logging
from mylib import do_something
from Suren.common import configure_logging

logger = logging.getLogger(__name__)

def main():
    configure_logging(level=logging.info)
    logger.info('Started')
    do_something()
    logger.info('Finished')

if __name__ == '__main__':
    main()







    

















