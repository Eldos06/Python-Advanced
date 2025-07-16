from asyncio import TaskGroup, run
from aiohttp import ClientSession
from common import setup_logging, log
import urllib.parse

# URL сервера (если сервер на другом хосте или порту — поменяй)
API_BASE = "http://127.0.0.1:8080"


def create_url(path: str) -> str:
    return urllib.parse.urljoin(API_BASE, path)


async def get_api(url: str) -> dict:
    async with ClientSession() as session:
        log.info(f"Fetching {url}")
        async with session.get(url) as response:
            response.raise_for_status()  # выбросит исключение при 404 или 500
            return await response.json()


async def run_main():
    async with TaskGroup() as tg:
        log.info("Starting API calls")
        stocks_task = tg.create_task(get_api(create_url("/stocks")))
        weather_task = tg.create_task(get_api(create_url("/weather")))

    # Получаем результаты после завершения TaskGroup
    stocks = await stocks_task
    weather = await weather_task

    log.info(f"Stocks: {stocks}")
    log.info(f"Weather: {weather}")


def main():
    setup_logging()
    run(run_main())


if __name__ == "__main__":
    main()
