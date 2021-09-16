def primes() -> list:
    temp = list()
    for num in range(2, 101):
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
        if prime:
            temp.append(num)
    return temp


if __name__ == "__main__":
    print(primes())
