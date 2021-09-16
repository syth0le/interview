import time


def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        finish = time.time()
        print(finish-start)
        return result
    return wrapper


@timer
def worker():
    time.sleep(3)
    return "I'm Done"


if __name__ == "__main__":
    worker()
