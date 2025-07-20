import logging

import urllib

from aiohttp import ClientSession

def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

def create_url(path: str) -> str:

    return urllib.parse.urljoin(base, path)


async def get_api(url: str) -> dict:
    async with ClientSession() as session:
        async with session.get(url) as response:
            log.info(f"Response url %s", response.url)
            return await response.json()

log = logging.getLogger(__name__)
