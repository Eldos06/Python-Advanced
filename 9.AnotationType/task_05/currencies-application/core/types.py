from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import TypedDict

# Описываем, как должен выглядеть "сырой" ответ с сервера (для аннотаций типов)
class ResponseType(TypedDict):
    date: date
    values: dict[str, Decimal]

# Класс для одной конкретной котировки (например: валюта="rub", значение=Decimal("72.24"))
@dataclass(frozen=True)  # frozen=True делает объект защищенным от изменений
class CurrencyValue:
    currency: str
    value: Decimal

# Главный класс-контейнер, который содержит дату, базовую валюту и список всех остальных курсов к ней
@dataclass(frozen=True)
class CurrencyInfo:
    date: date
    currency: str
    values: list[CurrencyValue]

    # Метод-фабрика. Он принимает сырые данные из API и собирает из них красивый объект нашего класса
    @classmethod
    def from_currency_info_response(
            cls,
            info: ResponseType,
            source_currency: str,
            target_currencies: set[str],
    ) -> "CurrencyInfo":
        return cls(
            # Конвертируем строку даты "2026-06-11" в специальный объект даты Python
            date = date.fromisoformat(info["date"]),
            currency = source_currency,
            # Пробегаемся циклом по всем валютам из интернета
            values = [
                # Создаем объект CurrencyValue для каждой валюты
                CurrencyValue(currency=name, value=value)
                for name, value in info["values"].items()
                # КРИТИЧЕСКИЙ МОМЕНТ: сохраняем только те валюты, которые есть в нашем TARGET_CURRENCIES (config.py)
                if name in target_currencies
            ],
        )