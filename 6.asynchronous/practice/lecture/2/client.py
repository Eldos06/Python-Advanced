from asyncio import TaskGroup, run
import asyncio
from aiohttp import ClientSession
from common import setup_logging, log
import urllib.parse
import sys

policy = asyncio.WindowsSelectorEventLoopPolicy()
asyncio.set_event_loop_policy(policy)



# Server URL (if the server is on another host or port — change this)
API_BASE = "http://127.0.0.1:8080"


def create_url(path: str) -> str:
    """
    Constructs a full API URL by joining the base URL with the given path.
    """
    return urllib.parse.urljoin(API_BASE, path)


async def get_api(url: str) -> dict:
    """
    Fetches JSON data from the specified API URL using an HTTP GET request.

    Args:
        url (str): The API endpoint URL.

    Returns:
        dict: The parsed JSON response from the API.

    Raises:
        Exception if the request fails or response is not JSON.
    """

    import aiohttp
    conn = aiohttp.TCPConnector(limit_per_host=5)


    async with ClientSession(connector=conn) as session:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.json()


async def run_main():
    """
    Orchestrates concurrent API calls to fetch stocks and weather data.
    """
    async with TaskGroup() as tg:
        log.info("Starting API calls")
        stocks_task = tg.create_task(get_api(create_url("/stocks")))
        weather_task = tg.create_task(get_api(create_url("/weather")))

        # Get the results after TaskGroup finishes
        stocks = await stocks_task
        weather = await weather_task

        log.info(f"Stocks: {stocks}")
        log.info(f"Weather: {weather}")

# Ensure compatibility with Windows event loop policy for Python 3.8+
if (sys.platform.startswith('win')
        and sys.version_info[0] == 3
        and sys.version_info[1] >= 8):
    policy = asyncio.WindowsSelectorEventLoopPolicy()
    asyncio.set_event_loop_policy(policy)

def main():
    setup_logging()


if __name__ == "__main__":
    setup_logging()
    run(run_main())
