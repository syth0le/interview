# Элементы по очереди, слева направо, добавляются в отсортированную часть массива.

array = [10, 12, 43, 34, 2, 4, 23, 5, 8, 94]
N = len(array)


def sort_insertion(n: int, arr: list[int]) -> list[int]:
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


print(sort_insertion(N, array))
