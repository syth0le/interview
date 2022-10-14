def fibonacci_generator():
    n = 0
    m = 1
    while True:
        yield n
        n, m = m, n + m



n = 0
for i in fibonacci_generator():
    if n == 5:
        break
    print(i)
    n += 1