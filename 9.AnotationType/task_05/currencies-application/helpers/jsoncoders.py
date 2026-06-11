import json
from datetime import date
from decimal import Decimal
from typing import Any

# Правило для конвертации нестандартных типов в JSON-строку
def json_encode_default(obj: Any) -> Any:
    if isinstance(obj, date):
        return obj.isoformat()  # Дату превращаем в строку формата "ГГГГ-ММ-ДД"
    if isinstance(obj, Decimal):
        return str(obj)         # Точное число Decimal превращаем в обычную строку (чтобы не потерять нули)
    raise TypeError(f"Type {type(obj)} not serializable")

# Функция, которая превращает любой Python-объект (словарь, список) в красивую JSON-строку
def json_encode(obj: Any) -> str: # json.dumps always return str
    return json.dumps(
        obj,
        ensure_ascii=False, # Разрешаем кириллицу и другие символы без экранирования
        indent=2,           # Делаем красивые отступы в 2 пробела (для читаемости)
        default=json_encode_default, # Подключаем наше правило выше
    )

# Специальный декодер: когда мы читаем JSON из сети, он автоматически превращает любые цифры в Decimal вместо float
json_decode_decimal = json.JSONDecoder(
    parse_int=Decimal,
    parse_float=Decimal,
)