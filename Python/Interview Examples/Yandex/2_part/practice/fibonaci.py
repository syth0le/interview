from time import sleep


def gen_fibonacci():
    n = 0
    m = 1
    while True:
        yield n
        n, m = m, n + m


for item in gen_fibonacci():
    print(item)
    sleep(0.5)  # чтобы показать что работает правильно, а то быстро отрабатывает и не видно


# Fibonacci as Iterator
# Iterator requires __next__ method

class FibIt:
    def __init__(self):
        self.a, self.b = 0, 1

    def __next__(self):
        return_value = self.a
        self.a, self.b = self.b, self.a + self.b
        return return_value

    def __iter__(self):
        return self


fib = FibIt()
for item in fib:
    print(item)
    sleep(0.5)

# while True:
#     print(next(fib))
#     sleep(0.5)

