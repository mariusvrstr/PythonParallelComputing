
import time
import random
from datetime import datetime
from threading import Thread

'''
In this example it is shown how running activities with i/o & wait time can still
have big performance improvements even though the GIL blocks concurrent CPU time
'''

# Used to track time spent in specific activities
class Stopwatch:
    start_time = None
    end_time = None

    def start(self):
        self.start_time = datetime.now()
        return self

    def stop(self):
        self.end_time = datetime.now()
        return self
    
    def elapsed_time_in_seconds(self):
        return (self.end_time - self.start_time).total_seconds()

# Shared Object to persist time spent across threads
class Counter:
    requests = dict()

    def add_request(self, sequence):
        self.requests[sequence] = None

    def add_response(self, sequence, time_in_seconds):
        self.requests[sequence] = time_in_seconds

    def total_time(self):
        total_time = 0
        for key in self.requests:
            total_time += self.requests[key]
        return total_time

    def calculate_time_saved(self, time_from_parent):
        actual_time = float(time_from_parent)
        execution_time = float(self.total_time())
        time_saved = execution_time - actual_time
        return time_saved

# Utility method to simulate real CPU workfload not just wait time
def simulate_cpu_workload(n):
    return sorted([random.random() for i in range(n)])

def exec(sequence, counter):
    print(f'Starting item request [{sequence}]')
    stopwatch = Stopwatch().start()
    
    # Simulate some i/o activity (This reduces with concurrency)
    time.sleep(1)

    # Simulate some CPU work (Queued with python's GIL)
    simulate_cpu_workload(1000)

    counter.add_response(sequence, stopwatch.stop().elapsed_time_in_seconds())

    print(f'Ending item request [{sequence}] in {stopwatch.elapsed_time_in_seconds()}s')

def main():

    '''
    Using memeory sharing, the object is created
    outside of the Threads and its reference passed through
    '''
    counter = Counter()
    print(f'Starting batch request')
    stopwatch = Stopwatch().start()

    thread_list = []

    # Add list of threads
    for i in range(5):
        new_thread = Thread(target=exec,args=(i,counter))
        thread_list.append(new_thread)

    # Start all the threads before joining them
    for thread in thread_list:
        thread.start()

    # Join them to wait until all is completed before continueing
    for thread in thread_list:
        thread.join()

    print('')
    print(f'Batch Ended. It took {stopwatch.stop().elapsed_time_in_seconds()}s to complete {counter.total_time()}s of work. Saving {(counter.calculate_time_saved(stopwatch.elapsed_time_in_seconds()))}s')

main()



