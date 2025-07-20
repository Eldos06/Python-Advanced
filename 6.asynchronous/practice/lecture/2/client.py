from asyncio import TaskGroup, run
import asyncio
from aiohttp import ClientSession
from common import configure_logging, log
import urllib.parse






# Server URL (if the server is on another host or port — change this)
API_BASE = "http://127.0.0.1:8080"


def create_url(base: str, path: str):
    return urllib.parse.urljoin(base, path)


def api_url(path: str) -> str:
    return urllib.parse.urljoin(API_BASE, path)


async def get_api(url: str) -> dict:
    async with ClientSession() as session:
        async with session.get(url) as response:
            log.info(f"Response url %s", response.url)
            return await response.json()


async def run_main():
    log.info("Run API calls")
    async with TaskGroup() as tg:
        stocks_task = tg.create_task(get_api(create_url("/stocks")))
        weather_task = tg.create_task(get_api(create_url("/weather")))

    log.info(f"Stocks: {stocks_task.result()}")
    log.info(f"Weather: {weather_task.result()}")

async def main():
    configure_logging()
    run(run_main())

if __name__ == "__main__":
    run(main())
