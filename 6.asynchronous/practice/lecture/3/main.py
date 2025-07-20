import os
import asyncio
import uvloop

if __name__ == "__main__":
    if 'nt' in os.name:
        asyncio.set_event_loop_policy(
            asyncio.WindowsSelectorEventLoopPolicy()
            )
    else:
        uvloop.install()