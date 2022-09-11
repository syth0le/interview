array = [10, 12, 43, 34, 2, 4, 23, 5, 8, 94]
N = len(array)


def sort_selection(n: int, arr: list[int]) -> list[int]:
    for i in range(n):
        minimum = i
        for j in range(i, n):
            if arr[minimum] > arr[j]:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr


print(sort_selection(N, array))
