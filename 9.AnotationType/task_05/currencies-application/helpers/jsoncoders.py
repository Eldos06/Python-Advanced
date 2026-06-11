import json
from datetime import date
from decimal import Decimal
import logging
from typing import Any

log = logging.getLogger(__name__)

# Правило для конвертации нестандартных типов в JSON-строку
def json_encode_default(obj: Any) -> Any:
    if isinstance(obj, date):
        return obj.isoformat()  # Дату превращаем в строку формата "ГГГГ-ММ-ДД"
    if isinstance(obj, Decimal):
        return str(obj)         # Точное число Decimal превращаем в обычную строку (чтобы не потерять нули)
    raise TypeError(f"Type {type(obj)} not serializable")

# Функция, которая превращает любой Python-объект (словарь, список) в красивую JSON-строку
"""
dumps расшифровывается как Dump String (вывалить в строку).
Этот метод берёт структуры данных Python (всякие там dict, list) и
превращает их в один длинный кусок текста (строку) в формате JSON.
Без этой функции ты не сможешь отдать данные браузеру, потому что браузер не знает, что такое dict в Python,
он понимает только текст!
"""
def json_encode(obj: Any) -> str: # json.dumps always return str
    log.info(f"json_encode_default({json_encode_default} \n\n obj: {obj} \n\n obj: {type(obj)})")
    # obj: {'date': datetime.date(2026, 6, 11), 'currency': 'usd', 'values': [{'currency': 'eur', 'value': Decimal('0.86599177')}, {'currency': 'inr', 'value': Decimal('95.64189642')}, {'currency': 'jpy', 'value': Decimal('160.51080253')}, {'currency': 'rub', 'value': Decimal('72.24271678')}, {'currency': 'usd', 'value': Decimal('1')}]}
    # obj: <class 'dict'>)
    return json.dumps(
        obj,
        ensure_ascii=False, # Разрешаем кириллицу и другие символы без экранирования
        indent=2,           # говорит: «Сделай мне красивый перенос строк и отступы в 2 пробела для каждого вложенного элемента». Получается красивая, читаемая лесенка.
        default=json_encode_default, # Подключаем наше правило выше
    )


# Специальный декодер: когда мы читаем JSON из сети, он автоматически превращает любые цифры в Decimal вместо float
json_decode_decimal = json.JSONDecoder(
    parse_int=Decimal,
    parse_float=Decimal,
)