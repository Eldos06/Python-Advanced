from aiohttp import web
from asyncio import sleep
from common import setup_logging, log

route = web.RouteTableDef()

@route.get("/stocks")
async def get_stocks(request: web.Request):
    await sleep(1)
    return web.json_response(
        data={"stocks": ["A", "B"], "prices": [100, 200]},
    )

@route.get("/weather")
async def get_weather(request: web.Request):
    return web.json_response(
        data={"weather": "sunny", "temperature": 25}
    )

def main():
    setup_logging()
    app = web.Application()
    app.add_routes(route)
    print("✅ Сервер запущен: http://127.0.0.1:8080")
    web.run_app(app, host="127.0.0.1", port=8080)

if __name__ == "__main__":
    main()
