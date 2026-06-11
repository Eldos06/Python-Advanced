import json
import logging
from dataclasses import asdict
from datetime import date
from typing import Iterator, Any, Iterable

import aiofiles  # Библиотека для асинхронной работы с файлами на диске
import aiohttp
from aiohttp import web

from core.config import CACHE_DIR, CURRENCIES_LIST_API_URL, TARGET_CURRENCIES, configure_logging, CURRENCY_API_URL
from core.types import CurrencyInfo, ResponseType
from helpers.jsoncoders import json_decode_decimal, json_encode

log = logging.getLogger(__name__)


class CurrencyRatesGetter:
    def __init__(
            self,
            currency: str,
            to_currency: Iterable[str] = TARGET_CURRENCIES,
            for_data: date | None = None,
    ) -> None:
        self.source_currency = currency.lower()
        self.target_currencies = {cur.lower() for cur in to_currency}
        self.for_data: date = for_data or date.today()
        self.selected_date = self.for_data.isoformat()

    # Формирует имя файла кэша. Пример: "2026-06-11-usd.json"
    @classmethod
    def get_cache_filename(cls, currency: str, for_date: date) -> str:
        return f"{for_date.isoformat()}-{currency}.json"

    # Шаг 1: Скачивание сырых данных из внешнего API в интернете
    async def request_currency_info(self) -> dict[str, Any]:
        # Подставляем имя валюты в наш URL из config.py
        url = CURRENCY_API_URL.format(currency=self.source_currency)

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as repr:
                # Если сервер упал или выдал 404, пресекаем падение и выдаем красивую ошибку 502
                if repr.status != 200:
                    msg = f"API returned status {repr.status} for URL: {url}"
                    raise web.HTTPBadGateway(
                        body=json.dumps({"message": msg}),
                        content_type="application/json"
                    )

                # Читаем данные, используя наш кастомный точный Decimal-декодер
                result = await repr.json(
                    loads=json_decode_decimal.decode,
                    content_type=None  # Игнорируем строгие заголовки типов сервера
                )
                return result

    # Шаг 2: Обработка скачанных данных и упаковка их в наш тип CurrencyInfo
    async def read_currency_info_for_date(self) -> CurrencyInfo:
        response_data = await self.request_currency_info()
        actual_date_str = response_data.get("date", self.selected_date)

        # Вытаскиваем из ответа только блок котировок для нашей валюты
        data: ResponseType = {
            "date": actual_date_str,
            "values": response_data[self.source_currency],
        }

        # Фильтруем и собираем готовый объект
        info = CurrencyInfo.from_currency_info_response(
            info=data,
            source_currency=self.source_currency,
            target_currencies=self.target_currencies,
        )
        return info

    # Шаг 3: Сохранение скачанного ответа на жесткий диск (Кэширование)
    @classmethod
    async def save_cached_currency_info(cls, info: CurrencyInfo) -> bytes:
        filename = cls.get_cache_filename(currency=info.currency, for_date=info.date)
        filepath = CACHE_DIR / filename

        # Превращаем объект дата-класса обратно в JSON-текст, а текст — в байты utf-8
        json_string = json_encode(asdict(info))
        info_data_bytes = json_string.encode("utf-8")

        # Асинхронно записываем байты в файл на диск
        async with aiofiles.open(filepath, "wb") as f:
            await f.write(info_data_bytes)
        return info_data_bytes

    # Связующий метод: скачал -> сохранил в кэш -> вернул байты
    async def read_and_save_currency_info(self) -> bytes:
        info = await self.read_currency_info_for_date()
        info_data_bytes = await self.save_cached_currency_info(info)
        return info_data_bytes

    # Шаг 4: Попытка прочитать данные из файла кэша без похода в интернет
    async def read_currency_info_from_cache(self) -> bytes | None:
        filename = self.get_cache_filename(currency=self.source_currency, for_date=self.for_data)
        filepath = CACHE_DIR / filename

        # Если файл с такой датой и валютой уже лежит в папке кэша
        if filepath.exists():
            # Асинхронно читаем его и сразу отдаем байты
            async with aiofiles.open(filepath, "rb") as file:
                return await file.read()
        return None  # Если файла нет — возвращаем None

    # ГЛАВНАЯ ТОЧКА ВХОДА КЛАССА
    async def get_currency_info(self) -> bytes:
        # Сначала проверяем кэш на диске
        cached = await self.read_currency_info_from_cache()
        if cached is not None:
            log.info("Taking rates from LOCAL CACHE")
            return cached

        # Если в кэше пусто — лезем в интернет
        log.info("Rates NOT found in cache, fetching from INTERNET")
        return await self.read_and_save_currency_info()

