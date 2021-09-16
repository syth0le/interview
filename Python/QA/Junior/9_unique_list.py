def duplicate_to_unique(arr: list) -> list:
    return list(set(arr))


if __name__ == "__main__":
    print(duplicate_to_unique([1, 1, 2, 3, 3]))
