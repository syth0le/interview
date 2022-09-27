# Реализовать генератор diff ,
# который возвращает разности между каждым элементом и предшествующим ему в некотором iterable.
# Пример:
# assert [1, 3, -5] == list(diff([3, 4, 7, 2]))
# [] [1] -> []
# [1, -1] -> [0]
# [5, 7 , 21] -> [2, 14]


def diff(lst: list[int]) -> generator:
    prev = None
    for item in lst:
        if prev:
            yield item - prev
        prev = item
