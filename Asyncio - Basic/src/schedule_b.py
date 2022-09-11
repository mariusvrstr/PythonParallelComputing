import asyncio

class ScheduleB():
    
    def exec(self, count):
        print(f'Do Schedule B - Tic {count}')
    
    async def start(self, delay):
        count = 1

        while True:
            self.exec(count)
            count += 1
            await asyncio.sleep(delay)