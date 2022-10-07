import threading, random, time


class Counter:

    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        th_name = threading.current_thread().name
        print(f'Th: {th_name} - ждет блокировку')
        self.lock.acquire()
        try:
            print(f'Th: {th_name} - получил блокировку')
            self.value = self.value + 1
        finally:
            self.lock.release()


def worker(c):
    for i in range(2):
        pause = random.random()
        th_name = threading.current_thread().name
        print(f'Th: {th_name} - заснул на {pause:0.02f}')
        time.sleep(pause)
        c.increment()
        print(f'Th: {th_name} - сделано.')


counter = Counter()
for i in range(2):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()

print('Ожидание рабочих потоков')
main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()
print(f'Счетчик: {counter.value}')
