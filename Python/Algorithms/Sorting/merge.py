# def merge_sort(arr: list) -> list:
#     length = len(arr)
#
#
#     return arr


def merge_sort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) or j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    print(result)
    return result


if __name__ == "__main__":
    print(merge_sort([4, 22, 41, 40, 27, 31, 36, 1, 42, 39, 14, 9, 3, 6, 34, 9, 21, 4, 29, 49]))
