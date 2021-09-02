def insertion_sort(arr: list) -> list:
    length = len(arr)
    for i in range(length):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(arr)

    return arr


if __name__ == "__main__":
    print(insertion_sort([4, 22, 41, 40, 27, 31, 36, 1, 42, 39, 14, 9, 3, 6, 34, 9, 21, 4, 29, 49]))
