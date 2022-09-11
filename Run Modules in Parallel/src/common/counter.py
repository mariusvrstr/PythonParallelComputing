from threading import Lock

class Counter:
    executed_count = 0
    _mutex = Lock()

    def incriment(self, incriment = 1):
        self._mutex.acquire()
        self.executed_count += incriment
        self._mutex.release()

    def get_number_of_executions(self):
        return self.executed_count