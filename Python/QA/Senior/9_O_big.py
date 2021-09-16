import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        time.sleep(1)
        finish = time.time()
        print(finish - start)
        return res
    return wrapper

@timer
def f1(arr):
    l1 = sorted(arr)
    l2 = [i for i in l1 if i < 0.5]
    return [i * i for i in l2]

@timer
def f2(arr):
    l1 = [i for i in arr if i<0.5]
    l2 = sorted(l1)
    return [i * i for i in l2]

@timer
def f3(arr):
    l1 = [i * i for i in arr]
    l2 = sorted(l1)
    return [i for i in l1 if i < (0.5*0.5)]


if __name__ == "__main__":
    test = [1, 3, 5, 9, 7, 5, 234, 324, 2435, 234,654, 234, 234245, 24523, 245, 345235,243,524,5,7,3,7,3,8,3,45,2,2,4]
    print(f1(test))
    print(f2(test))
    print(f3(test))

