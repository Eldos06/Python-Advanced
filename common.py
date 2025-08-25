# common.py
import logging
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

def configure_logging(
        level: int = logging.INFO,
) -> logging.Logger:
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H-%M-%S",
        format="%(module)5s:%(lineno)-3d %(levelname)-7s - %(message)s",
    )
    return logging.getLogger(__name__)

log = configure_logging(logging.INFO)


