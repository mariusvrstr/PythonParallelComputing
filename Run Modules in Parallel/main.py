from itertools import count
from ntpath import join
import time
from threading import Thread
from src.common.counter import Counter
from src.module_a import ModuleA
from src.module_b import ModuleB

def main():
    counter = Counter()

    module_a = ModuleA()
    thread_a = Thread(target=module_a.start, args=(counter,))
    thread_a.start()

    module_b = ModuleB()
    thread_b = Thread(target=module_b.start, args=(counter,))
    thread_b.start()

    thread_a.join()
    thread_b.join()

    print(f'Completed all threads. Total of [{counter.executed_count}] executions')

main()




