import logging
from common import configure_logging

logger = logging.getLogger(__name__)

def divide(a, b):
    logger.error("divide is started")
    configure_logging(level=logging.ERROR)  # Лучше вызывать это один раз в main
    try:
        return a / b
    except ZeroDivisionError as e:
        logger.error("Attempted to divide by zero: a=%s, b=%s", a, b)
        # либо повторно выбрасывать ошибку, если нужно прервать выполнение
        raise ZeroDivisionError("A very specific bad thing happened.") from e


if __name__ == "__main__":
    try:
        result = divide(10, 0)
        print(result)
    except ZeroDivisionError as e:
        logger.exception("An error occurred during division.")
