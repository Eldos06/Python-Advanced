import asyncio
import logging
# from time import sleep
from asyncio import sleep
from random import randint, random


logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y-%m-%d %H-%M-%S",
    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s",
                    )


log = logging.getLogger(__name__)

async def get_stocks():
    log.info("getting stock")
    for s in range(1, 6):
        log.info("s %s ^ 3 = %s", s, s**3)
        await asyncio.sleep(0.001)
    log.info("got stock")
    return {"stocks": []}

async def get_weather():
    log.info("getting weather")
    for w in range(1, 51):
        log.info("w %s ^ 2 = %s", w, w**2)
        await asyncio.sleep(0)
    await asyncio.sleep(1)
    log.info("got weather")
    return {"weather" : {}}

# async def main():
#     log.info("start!")
#     coro = get_stocks()
#     log.info("created coro %s", coro)
#     stocks, weather = await asyncio.gather(
#         coro,
#         get_weather()
#     )
#     log.info("Stocks: %s", stocks)
#     log.info("Weather: %s", weather)
#     log.info("Done!")

async def get_stock(name: str) -> int:
    log.info("Get stock %r", name)
    to_sleep = random()
    if random > 0.4:
        log.warning("get stock %s error", name)
        raise ValueError(name)

    await asyncio.sleep(to_sleep)
    price = randint(1,500)  
    log.info("Got stock %r for %s", name, price)
    return {'name': name, 'price': price}

async def get_n_stocks(n_stock: int):
    log.info("Get %s stocks", n_stock)
    tasks = {
        asyncio.create_task(
            get_stock(name=f"Kaspi {i:03}"),
            name=f"get-stock-{i}"
        )
        for i in range(1, n_stock+1)
    }
    done, pending = await asyncio.wait(tasks)
    for task in pending:
        task.cancel()

    for task in done:    
        log.info("Got %s stocks", n_stock)

async def main():
    await get_n_stocks(10)

# async def main():
#     log.info("start!")
#     coro = get_stocks()
#     log.info("created coro %s", coro)
#     async with asyncio.TaskGroup() as tg:
#         task_stock = tg.create_task(coro)
#         task_weather = tg.create_task(get_weather())
#     stocks = task_stock.result()
#     log.info("Stocks: %s", stocks)
#     weather = task_weather.result()
#     log.info("Weather: %s", weather)
#     log.info("Done!")
    

asyncio.run(main())






























