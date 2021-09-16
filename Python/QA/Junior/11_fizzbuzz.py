def fizzbuzz_checker(num: int) -> str:
    temp = ''
    if num % 3 == 0:
        temp += "Fizz"
    if num % 5 == 0:
        temp += "Buzz"
    return temp


def fizzbuzz() -> None:
    list(map(lambda x: print(x, fizzbuzz_checker(x)) if fizzbuzz_checker(x) != '' else None, range(1, 20)))
    # for elem in range(1, 20):
    #     if fizzbuzz_checker(elem) != '':
    #         print(elem, fizzbuzz_checker(elem))


if __name__ == "__main__":
    print(fizzbuzz())
