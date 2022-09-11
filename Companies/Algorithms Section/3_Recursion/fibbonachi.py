# БЕЗ РЕКУРСИИ САМОЕ ЭФФЕКТИВНОЕ
N = 10


def fib_optimal(n):
    if n < 1:
        return 1
    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current


print(fib_optimal(N))


# C рекурсией

def fib_recursion(n):
    if n <= 2:
        return 1
    return fib_recursion(n - 1) + fib_recursion(n - 2)


print(fib_recursion(N))
