# Выбирается элемент. Все меньшие элементы переносятся в левую часть, бо́льшие — в правую.
# Затем алгоритм вызывается рекурсивно от левой и правой частей.

array = [10, 12, 43, 34, 2, 4, 23, 5, 8, 94]
N = len(array)


def quick_sort(arr: list[int]) -> list[int]:
    length = len(arr)
    if length < 2:
        return arr
    left = []
    same = []
    right = []
    element = arr[length // 2]  # arr[randint(0, len(array) - 1)]
    for item in arr:
        if item < element:
            left.append(item)
        if item == element:
            same.append(item)
        if item > element:
            right.append(item)
    return quick_sort(left) + same + quick_sort(right)


print(quick_sort(array))
