import asyncio
from currency_exist_check import CurrencyExistCheck
from currency_rates_getter import CurrencyRatesGetter
from types import CurrencyInfo

async def main():
    # Проверим, существует ли валюта
    checker = CurrencyExistCheck()
    exists = await checker.currency_exists("usd")
    print(f"USD exists: {exists}")

    # Получим курсы валют
    getter = CurrencyRatesGetter("usd")
    print(f"Fetching rates for {getter.currency} on {getter.for_date}")
    # Здесь нужно будет реализовать метод загрузки курсов в CurrencyRatesGetter

if __name__ == "__main__":
    asyncio.run(main())
