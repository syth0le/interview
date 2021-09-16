def binary_to_int(string: str) -> int:
    acc = 0
    length = len(string)
    string = string[::-1]
    for i in range(length):
        if string[i] == "1":
            acc += 2 ** i

    return acc


if __name__ == "__main__":
    print(binary_to_int("1011"))
