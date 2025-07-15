import logging
from common import configure_logging
from utils import do_something

log = logging.getLogger(__name__)

know_weather = {
    
    "sochi" : {"rain_chance": 23},

}

def get_weather() -> dict | None :
    ero_dev_err = None
    try:
        1/0
    except ZeroDivisionError as e:
        zero_dev_err = e

    log.debug(
        "Zero division error: %r",
        zero_dev_err,
        exc_info=zero_dev_err,
    )

    try:
        return know_weather[city.lower()]
    except KeyError:
        log.exception("Couldn't find city")
        return None
    
    

def main():
    configure_logging(level=logging.DEBUG)
    log.warning("Hello! Starting main")
    get_weather("Almaty")
    log.warning("Done doing something")

if __name__ == "__main__":
    main()



