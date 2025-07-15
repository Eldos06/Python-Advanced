import logging
import time

from config import config
from exceptions import RequestError

log = logging.getLogger(__name__)


class CustomWeatherFetcher:
    def __init__(self):
        self._call_count = 0

    def fetch_weather_or_raise_error(
        self,
        url: str,
        timeout: int,
        headers: dict[str, str] | None,
    ) -> dict[str, str | int]:
        """
        Функция, которая в зависимости от номера попытки
        либо выкидывает исключение, либо отрабатывает нормально.

        Такое поведение возможно только для демонстрации,
        перед новой демонстрацией необходимо сбрасывать счётчик.
        """
        self._call_count += 1

        log.debug(
            "Fetching data from %s with headers %s. Will take %ss",
            url,
            headers,
            timeout,
        )
        time.sleep(timeout)
        if self._call_count == config.success_on_attempt:
            return {"temperature": 16, "rain-chance": 42, "sky": "clouds"}
        msg = f"failed to fetch data from {url} with headers {headers}"
        raise RequestError(msg)

    def reset_call_count(self):
        self._call_count = 0


weather_fetcher = CustomWeatherFetcher()