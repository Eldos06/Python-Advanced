import logging
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent
CACHE_DIR = BASE_DIR / 'currencies-data-cache'

CURRENCIES_LIST_API_URL = (
  'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api'
  '@latest/v1/currencies.json'
)

CURRENCIES_API_URL = (
  "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api"
  "@{date}/v1/currencies/{currency}.json"
)

TARGET_CURRENCIES = ('rub', 'usd', 'eur', 'inr', 'jpy')

DEFAULT_FORMAT = (
  "[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s"
)

log = logging.basicConfig(
                          level=logging.INFO,
                          format=DEFAULT_FORMAT,
                          datefmt='%Y-%m-%d %H:%M:%S',
                          handlers=[
                              logging.FileHandler("file.log"),
                              logging.StreamHandler()
                          ],
                          )
log = logging.getLogger(__name__)