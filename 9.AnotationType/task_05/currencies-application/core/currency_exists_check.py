import logging
from dataclasses import dataclass, field
import aiohttp
from core import config

log = logging.getLogger(__name__)


@dataclass
class CurrencyExistsCheck:
    # Множество для хранения списка валют в оперативной памяти (чтобы не скачивать его каждую секунду)
    cache_currencies: set[str] = field(default_factory=set)

    # Асинжеронная функция, которая скачивает справочник валют из интернета
    @classmethod
    async def get_all_currencies(cls) -> dict[str, str]:
        log.info("Fetching all currencies")
        async with aiohttp.ClientSession() as session:
            # Делаем HTTP GET запрос к справочнику
            async with session.get(config.CURRENCIES_LIST_API_URL) as response:
                # Читаем ответ как JSON-словарь
                data: dict[str, str] = await response.json()
                return data

    # Функция проверки: существует валюта или нет
    async def currency_exists(self, currency: str) -> bool:
        # Если наш внутренний кэш пустой — скачиваем справочник один раз
        if not self.cache_currencies:
            all_currencies = await self.get_all_currencies()
            # Закидываем все ключи (коды валют) в наш внутренний set
            self.cache_currencies.update(set(all_currencies))

        # Возвращает True, если переданная валюта есть в мировом списке, иначе False
        return currency in self.cache_currencies


# Создаем один глобальный объект для импорта в другие файлы
check = CurrencyExistsCheck()