import asyncio
import logging
import common
from aiohttp import web
from asyncio import sleep

# from flask import logging
from common import configure_logging, log


log = logging.getLogger(__name__)
route = web.RouteTableDef()

# STOCKS_API_BASE = "http://openexchangerates.org/"
# WEATHER_API_BASE = "http://api.open-meteo.com/"


@route.get("/stocks")
async def get_stocks(request: web.Request):
    log.info("Fetching stocks data")
    # TODO: Simulate a delay for fetching stocks data
    await asyncio.sleep(1)
    log.info("Stocks data fetched successfully")
    return web.json_response(
        data={"stocks": ["A", "B"]},
    )

@route.get("/weather")
async def get_weather(request: web.Request):
    return web.json_response(
        data={"weather": "sunny", "temperature": 25}
    )

def main():
    configure_logging()
    app = web.Application()
    app.add_routes(route)
    # Add CORS support
    try:
        import aiohttp_cors
        cors = aiohttp_cors.setup(app)
        for route_obj in list(app.router.routes()):
            cors.add(route_obj)
    except ImportError:
        print("aiohttp_cors not installed, skipping CORS setup.")
    print("✅ Server started: http://127.0.0.1:8080")
    try:
        web.run_app(app, host="127.0.0.1", port=8080)
    except Exception as e:
        print(f"❌ Server startup error: {e}")

if __name__ == "__main__":
    main()
