import asyncio
from types import coroutine

from src.module_a import ModuleA
from src.module_b import ModuleB

async def register_schedules():
    asyncio.ensure_future(ModuleA().start(1))
    asyncio.ensure_future(ModuleB().start(2))

def main():
    loop = asyncio.get_event_loop()
    try:
        asyncio.ensure_future(register_schedules())
        loop.run_forever()
    finally:
        loop.close()

main()
