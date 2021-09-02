def bubble_sort(arr: list) -> list:
    length = len(arr)
    for i in range(length):
        for j in range(length - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == "__main__":
    print(bubble_sort([15, 12, 4, 54, 14, 1, 4, 51, 5]))
