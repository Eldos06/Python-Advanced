import logging


# удобная функция, как print()
def log(message, *args, level=logging.INFO, **kwargs):
    logging.log(level, str(message), *args, **kwargs)

def configure_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        format="[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-8s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

