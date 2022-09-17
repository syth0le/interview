# написать функцию getPrimes(n)
# Возвращает простые числа от 2 до n

def getPrimes(n):
    res = []
    for i in range(2, n+1):
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                isPrime = False
        if isPrime:
            res.append(i)

    return res


print(getPrimes(256))
