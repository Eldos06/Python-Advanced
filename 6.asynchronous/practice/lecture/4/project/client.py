import aiohttp
import asyncio
from common import log
import logging
from functools import cache
import aiofiles
import aiofiles.os



log = logging.getLogger(__name__)


@cache
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/eur.json') as resp:
            log.info(resp.status)
            print('------------------')
            data = await resp.json()
            rates = data["eur"]  # потому что URL: .../eur.json
            for target in ['usd', 'kzt', 'eur']:
                log.info(f"{target.upper()}: {rates.get(target)}")

async def writeFile():
    async with aiofiles.open('currencies.txt', mode='w') as f:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/eur.json') as resp:
                data = await resp.json()
                rates = data["eur"]
                for target in ['usd', 'kzt', 'eur']:
                    try:
                        await f.write(f"{target.upper()}: {rates.get(target)}\n")
                    except Exception as e:
                        log.error(f"Error writing {target}: {e}")


async def readFile():
    async with aiofiles.open('currencies.txt', mode='r') as f:
        async for line in f:
            print(line.strip())





asyncio.run(main())
asyncio.run(writeFile())
asyncio.run(readFile())














