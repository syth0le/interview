import time


def decorator(func):
    def wrapper(*args, **kw):
        start = time.time()
        result = func(*args, **kw)
        finish = time.time()
        print('%r  %2.2f ms' % (func.__name__, (start - finish) * 1000))
        return result, finish - start

    return wrapper


@decorator
def func(num: int) -> int:
    for _ in range(num):
        i = 0
    return -1


if __name__ == "__main__":
    print(func(120000))

    print(",".join(map(str, [1, 34, 1234, 2])))
