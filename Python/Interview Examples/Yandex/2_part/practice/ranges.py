# Дан список интов, повторяющихся элементов в списке нет. Нужно преобразовать это множество в строку,
# сворачивая соседние по числовому ряду числа в диапазоны. Примеры:
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"

def make_prettier(start: int, finish: int) -> str:
    if start == finish:
        return f'{finish},'
    return f'{start}-{finish},'


def get_ranges(arr: list[int]) -> str:
    if not arr:
        return ''
    arr.sort()
    res = ''
    prev = None
    start = None
    for item in arr:
        if prev is None:
            start = item
            prev = item
            continue
        if item == prev + 1:
            prev = item
        else:
            res += make_prettier(start, prev)
            start = item
            prev = item
    if prev == arr[-1]:
        res += make_prettier(start, prev)
    return res[:-1]


print(get_ranges([1, 4, 5, 2, 3, 9, 8, 11, 0]))
print(get_ranges([1, 4, 3, 2]))
print(get_ranges([1, 4]))
