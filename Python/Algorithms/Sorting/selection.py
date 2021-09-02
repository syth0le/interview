def selection_sort(arr: list) -> list:
    length = len(arr)

    for i in range(length):
        lowest = i
        for j in range(i+1, length):
            if arr[j] < arr[lowest]:
                lowest = j

        arr[i], arr[lowest] = arr[lowest], arr[i]
        print(arr)

    return arr


if __name__ == "__main__":
    print(selection_sort([15, 12, 4, 54, 14, 1, 4, 51, 5]))
