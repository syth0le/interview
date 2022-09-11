# Метод двух указателей работает для сортированного массива
# пример решения задачи two_sum

array = [10, 12, 43, 34, 2, 4, 23, 5, 8, 94]
array.sort()
N = len(array)
target = 22


def two_pointers(n, arr, target):
    first, second = 0, n - 1
    while first < second:
        if arr[first] + arr[second] == target:
            return True
        elif arr[first] + arr[second] > target:
            second -= 1
        else:
            first += 1
    return False


print(two_pointers(N, array, target))