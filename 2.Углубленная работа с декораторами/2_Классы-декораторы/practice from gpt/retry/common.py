import logging
from exceptions import RequestError

log = logging.getLogger(__name__)


def run_example(func):
    log.info("*** Run func %s", func.__name__)
    try:
        data = func("https://example.org/weather", headers={"spam": "eggs"})
    except RequestError:
        log.exception("!!! Failed to fetch weather data")
        # log.error("Failed to fetch weather data")
    else:
        log.info("+++ Got data: %s", data)