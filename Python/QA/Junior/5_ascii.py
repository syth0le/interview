def ascii_converter(string: str) -> int:
    x = "".join(map(str, tuple(map(ord, string))))
    return x


if __name__ == "__main__":
    print(ascii_converter("abcd"))
