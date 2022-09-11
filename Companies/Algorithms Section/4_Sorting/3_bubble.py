array = [10, 12, 43, 34, 2, 4, 23, 5, 8, 94]
N = len(array)


def sort_bubble(n: int, arr: list[int]) -> list[int]:
    for i in range(n):
        for j in range(n):
            if arr[i] < arr[j]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr


print(sort_bubble(N, array))
