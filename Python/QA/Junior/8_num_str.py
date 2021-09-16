def num_to_str() -> str:
    return "".join(tuple(map(str, range(0, 100))))


if __name__ == "__main__":
    print(num_to_str())
