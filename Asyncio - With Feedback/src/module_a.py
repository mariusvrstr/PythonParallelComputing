import asyncio

class ModuleA():
    
    def exec(self, count):
        print(f'Do Module A - Tic {count}')
    
    async def start(self, delay):
        count = 1

        while True:
            self.exec(count)
            count += 1
            await asyncio.sleep(delay)

    
