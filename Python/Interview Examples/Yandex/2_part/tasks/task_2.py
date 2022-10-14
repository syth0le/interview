def compress(lst):
    if not lst or lst is None:
        return ''

    last = lst[-1]

    lst.sort()
    start = prev = None
    res = []

    for item in lst:
        if start is None:
            start = prev = item
            continue
        if item != prev + 1:
            temp = f'{start}-{prev},' if prev != start else f'{prev},'
            res.append(temp)
            prev = start = item
        else:
            prev = item

    temp = f'{start}-{prev}' if prev != start else f'{prev}'
    res.append(temp)
    return ''.join(res)


@pytest.mark.parametrize(
    'example, result',
    (
            ([], ''),
            ([1, 2,  3,  5,  6,  7,  20], '1-3,5-7,20'),
            ([1], '1'),
            ([1,  2,  3,  5,  6,  7], '1-3,5-7'),
    ),
)
def test_compress(example, result):
    compressed = compress(example)
    assert result == compressed
