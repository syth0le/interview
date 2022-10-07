from time import sleep


def gen_fibonaci():
    n = 0
    m = 1
    while True:
        yield n
        n, m = m, n + m


for item in gen_fibonaci():
    print(item)
    sleep(0.5)  # чтобы показать что работает правильно, а то быстро отрабатывает и не видно
