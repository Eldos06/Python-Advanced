from aiohttp import web
from asyncio import sleep
import logging

log = logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S",

    )
log = logging.getLogger(__name__)

route = web.RouteTableDef()
app = web.Application()
app.add_routes(route)


@route.get("/stocks")
async def get_stock():
    # Simulating a delay for fetching stock data
    log.info("Fetching stocks...")
    await sleep(1)
    log.info("Stocks fetched successfully")
    return web.json_response(
        data = {"stocks": ["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA"]},
    )


async def get_weather():
    # Simulating a delay for fetching weather data
    log.info("Fetching weather...")
    await sleep(1)
    log.info("Weather fetched successfully")
    return web.json_response(
        data = {"weather": "sunny", "temperature": 25}
    )

def main( ):
    web.run_app(app, port=8080)

if __name__ == "__main__":
    main()