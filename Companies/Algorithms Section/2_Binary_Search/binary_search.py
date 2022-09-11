array = [10, 12, 43, 34, 2, 4, 23, 5, 8, 94]
N = len(array)
target = 42
# для бинарного поиска массив должен быть уже отсортирован
array.sort()


def binary_search(n, array, target):
    left, right = 0, n
    while left < right:
        middle = (left + right) // 2
        if array[middle] == target:
            return True
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle


print(binary_search(N, array, target))


def binary_search_not_ok(n, array, target):
    temp = n // 2
    for i in range(n):
        if array[temp+1] < target:
            pass
        elif array[temp+1] > target:
            pass
        else:
            return temp+1
        temp = i