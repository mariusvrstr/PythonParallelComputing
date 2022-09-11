import time

class ModuleB:

    def start(self, counter):
        print('Module B Start')
        time.sleep(4)
        counter.incriment()
        print('Module B End')