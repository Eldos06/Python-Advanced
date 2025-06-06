from dataclasses import dataclass

DEFAULT_LOG_FORMAT = (
    "[%(asctime)s.%(msecs)03d] %(module)16s:%(lineno)-3d %(levelname)-7s - %(message)s"
)


@dataclass
class Config:
    success_on_attempt: int = 3


config = Config(
    success_on_attempt=4,
)
    