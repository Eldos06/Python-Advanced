import logging
from dataclasses import dataclass, field

import aiohttp
from common import log, CURRENCIES_LIST_API_URL

log = logging.getLogger(__name__)

@dataclass
class CurrencyExistCheck:
    cached_currencies: set = field(default_factory=set)

    @classmethod
    async def get_all_currencies(cls) -> dict[str]:
        log.info("Fetching all currencies from API")
        async with aiohttp.ClientSession() as session:
            async with session.get(CURRENCIES_LIST_API_URL) as response:
                return await response.json()

    async def currency_exists(self, currency: str) -> bool:
        if not self.cached_currencies:
            all_currencies = await self.get_all_currencies()
            self.cached_currencies.update(all_currencies.keys())
        return currency in self.cached_currencies



