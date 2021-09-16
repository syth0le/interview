def fib(start: int, next: int, stop: int):
    print(start)

    if next > stop:
        return "Stopped"

    fib(start=next, next=start+next, stop=stop)


def rec_fib(n):
    '''inefficient recursive function as defined, returns Fibonacci number'''
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n


if __name__ == "__main__":
    fib(0, 1, 10000)
