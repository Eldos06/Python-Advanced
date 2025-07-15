import logging

from common import run_example
from config import DEFAULT_LOG_FORMAT
from retry_class_dec import Retry, default_retry
from weather_fetcher import weather_fetcher

log = logging.getLogger(__name__)


@Retry(
    max_retry_count=5,
    initial_timeout=3,
    timeout_multiplier=2,
)
def fetch_weather_example_1(
    url: str,
    timeout: int = 1,
    headers: dict[str, str] | None = None,
) -> dict[str, str | int]:
    return weather_fetcher.fetch_weather_or_raise_error(
        url=url,
        timeout=timeout,
        headers=headers,
    )


@default_retry
def fetch_weather_example_2(
    url: str,
    timeout: int = 1,
    headers: dict[str, str] | None = None,
) -> dict[str, str | int]:
    return weather_fetcher.fetch_weather_or_raise_error(
        url=url,
        timeout=timeout,
        headers=headers,
    )


def main() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format=DEFAULT_LOG_FORMAT,
    )
    run_example(fetch_weather_example_1)
    weather_fetcher.reset_call_count()
    run_example(fetch_weather_example_2)


if __name__ == "__main__":
    main()