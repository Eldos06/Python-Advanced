import logging
import pathlib

# Определяем путь к папке, где лежит этот файл конфигурации
BASE_DIR = pathlib.Path(__file__).resolve().parent

# Создаем путь для папки кэша, где будут храниться скачанные курсы (в формате файлов .json)
CACHE_DIR = BASE_DIR / "currencies-data-cache"

# URL №1: Ссылка на актуальные курсы валют. {currency} — это шаблон, куда Python подставит нужную валюту (например, usd)
CURRENCY_API_URL = "https://latest.currency-api.pages.dev/v1/currencies/{currency}.json"

# URL №2: Ссылка на полный список существующих в мире валют (нужен для проверки опечаток)
CURRENCIES_LIST_API_URL = "https://latest.currency-api.pages.dev/v1/currencies.json"

# Кортеж (список) валют, которые нам интересны. Все остальные валюты из интернета приложение будет игнорировать
TARGET_CURRENCIES = (
    "rub",
    "usd",
    "eur",
    "inr",
    "jpy",
)

# Шаблон для красивого вывода логов в консоль (время, имя файла, строка, тип сообщения)
DEFAULT_FORMAT = (
    "[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s"
)

# Функция для включения и настройки логирования
def configure_logging(level: int = logging.INFO) -> None:
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format=DEFAULT_FORMAT,
    )