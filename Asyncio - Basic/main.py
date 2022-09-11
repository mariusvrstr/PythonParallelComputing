import asyncio
from types import coroutine

from src.schedule_a import ScheduleA
from src.schedule_b import ScheduleB

async def register_schedules():
    asyncio.ensure_future(ScheduleA().start(1))
    asyncio.ensure_future(ScheduleB().start(2))

def main():
    loop = asyncio.get_event_loop()
    try:
        asyncio.ensure_future(register_schedules())
        loop.run_forever()
    finally:
        loop.close()

main()





