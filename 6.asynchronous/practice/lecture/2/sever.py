import asyncio
from aiohttp import web
from asyncio import sleep
from common import setup_logging
import sys

# Ensure compatibility with Windows event loop policy for Python 3.8+
policy = asyncio.WindowsSelectorEventLoopPolicy()
asyncio.set_event_loop_policy(policy)

route = web.RouteTableDef()

@route.get("/stocks")
async def get_stocks(request):
    await sleep(1)
    return web.json_response(
        data={"stocks": ["A", "B"], "prices": [100, 200]},
    )

@route.get("/weather")
async def get_weather(request):
    return web.json_response(
        data={"weather": "sunny", "temperature": 25}
    )

def main():
    setup_logging()
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

# Ensure compatibility with Windows event loop policy for Python 3.8+
if (sys.platform.startswith('win')
        and sys.version_info[0] == 3
        and sys.version_info[1] >= 8):
    policy = asyncio.WindowsSelectorEventLoopPolicy()
    asyncio.set_event_loop_policy(policy)

if __name__ == "__main__":
    main()
