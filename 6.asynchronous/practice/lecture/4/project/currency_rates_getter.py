from dataclasses import asdict
from datetime import date
from typing import iterable

import aiohttp
import aiofiles

from common import CACHE_DIR, CURRENCIES_API_URL, TARGET_CURRENCIES
from currency_types import CurrencyInfo, ResponseType
from json_coders import json_decoder_decimal, json_encod
class CurrencyRatesGetter:

  def __init__(
      self,
      currency: str,
      to_currencies: iterable[str] = TARGET_CURRENCIES,
      for_date: date | None = None,
      ) -> None:
      self.currency = currency.lower()
      self.to_currencies = {cur.lower() for cur in to_currencies}
      self.for_date: date = for_date or date.today()
      self.selected_currencies = self.for_date.isoformat()

  @classmethod
  def get_cache_filename(
     cls,
     currency: str,
     for_date: date,
  ) -> str:
     return f"{for_date.isoformat()}-{currency}.json"



