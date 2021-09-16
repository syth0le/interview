from typing import Tuple

A = (9, 2, 4, 5, 1, 3)
B = (9, 2, 4, 5, 1, 3, 12)


def containsTuples(a: tuple, b: tuple) -> Tuple[bool, bool, bool]:
    sets = set(a).issubset(b) if len(b) > len(a) else set(b).issubset(a)
    set_a = True if len(set(a)) == len(a) else False
    set_b = True if len(set(b)) == len(b) else False
    return sets, set_a, set_b


if __name__ == "__main__":
    print(containsTuples(a=B, b=A))
    print(containsTuples(a=A, b=B))
