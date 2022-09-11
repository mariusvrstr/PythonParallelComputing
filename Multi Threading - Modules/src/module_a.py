import time

'''
Simple execute once logic
'''
class ModuleA:

    def start(self, counter):
        print('Module A Start')
        time.sleep(2)
        counter.incriment()
        print('Module A End')
        print('')
        