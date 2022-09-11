# Массив делится пополам, сортировка рекурсивно вызывается для обеих частей, затем создаётся временный массив,
# в который по порядку складываются значения из обеих частей.


array = [10, 12, 43, 34, 2, 4, 23, 5, 8, 94]
N = len(array)


def merge_sort(arr: list[int]) -> list[int]:
    def merge_lists(left, right):
        if len(left) == 0:
            return right
        if len(right) == 0:
            return left
        res = []
        idx_left = idx_right = 0
        while len(res) < len(left) + len(right):
            if left[idx_left] <= right[idx_right]:
                res.append(left[idx_left])
                idx_left += 1
            else:
                res.append(right[idx_right])
                idx_right += 1

            if idx_right == len(right):
                res += left[idx_left:]
                break
            if idx_left == len(left):
                res += right[idx_right:]
                break
        return res

    length = len(arr)
    if length < 2:
        return arr
    current = length // 2
    left = merge_sort(arr[:current])
    right = merge_sort(arr[current:])
    return merge_lists(left, right)


print(merge_sort(array))
