# ✅ Write an async function that waits 2 seconds and returns "Hello".
import asyncio
from random import random
import logging
from asyncio import run, sleep



logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y-%m-%d %H-%M-%S",
    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s",
                    )

log = logging.getLogger(__name__)

async def hell0():
    log.info("Starting ...")
    await sleep(2)
    log.info("Hello")
    log.info("Done")

# run(hell0())

#✅ Create 3 async functions that return different numbers, and gather their results.

import asyncio
import logging
import random

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

async def first():
    await asyncio.sleep(0.5)
    return random.randint(1, 100)

async def second():
    await asyncio.sleep(0.2)
    return random.randint(1, 100)

async def third():
    await asyncio.sleep(0.3)
    return random.randint(1, 100)

async def main():
    log.info("Starting! ...")

    results = await asyncio.gather(
        first(),
        second(),
        third()
    )

    log.info(f"Results: {results}")
    log.info("Done !!!")

# Run the program
# asyncio.run(main())

# ✅ Simulate checking the weather in 3 cities using asyncio.gather.

async def ShymWeather():
    log.info("Checking weather in Shymkent ... ")
    await sleep(1.05)
    log.info("Checked weather in Shymkent!")

async def AstWeather():
    log.info("Checking weather in Astana ... ")
    await sleep(1.02)
    log.info("Checked weater in Astana!")

async def AlmaWeather():
    log.info("Checking weather in Almata ... ")
    await sleep(1.03)
    log.info("Checked weather in Almata!")

async def main():
    await asyncio.gather(
        ShymWeather(),
        AstWeather(),
        AlmaWeather(),
        )

# run(main())