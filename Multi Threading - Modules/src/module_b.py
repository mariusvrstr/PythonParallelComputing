import asyncio

class ScheduleA():
    def exec(self, count):
        print(f'Do Schedule A - Tic {count}')
    
    async def start(self, delay):
        count = 1

        while True:
            self.exec(count)
            count += 1
            await asyncio.sleep(delay)

class ScheduleB():
    def exec(self, count):
        print(f'Do Schedule B - Tic {count}')
    
    async def start(self, delay):
        count = 1

        while True:
            self.exec(count)
            count += 1
            await asyncio.sleep(delay)

class ModuleB:

    async def register_schedules(self):
        asyncio.ensure_future(ScheduleA().start(1))
        asyncio.ensure_future(ScheduleB().start(2))

    def start(self):
        print('Module B - Start')
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        try:
            asyncio.ensure_future(self.register_schedules())
            loop.run_forever()
        finally:
            loop.close()
        
        print('Module B - End')
        print('')

        