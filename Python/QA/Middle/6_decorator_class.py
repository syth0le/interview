from time import time


class Timer:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time()
        result = self.func(*args, **kwargs)
        finish = time()
        print(finish-start)
        return result


class ErrorHandler:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            result = self.func(*args, **kwargs)
            return result
        except TypeError as e:
            print(f"ERROR FOUND!!!! {e.args}")


def decorator(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        finish = time()
        print(finish - start)
        return result
    return wrapper


@ErrorHandler
@decorator
@Timer
def some_worker(num: int):
    for i in range(num):
        print(i**2)


if __name__ == "__main__":
    some_worker('''dsjlfsljdfjlsdf''')
