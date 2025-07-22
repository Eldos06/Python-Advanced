import aiohttp
import asyncio
from common import log
import logging
log = logging.getLogger(__name__)

async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:

            log.info("Status:", response.status)
            log.info("Content-type:", response.headers['content-type'])

            html = await response.text()
            log.info("Body:", html[:15], "...")

asyncio.run(main())