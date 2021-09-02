from typing import Union


class Tree:

    def __init__(self, data: Union[int, str],
                 right: Union[int, str] = None,
                 left: Union[int, str] = None):
        self._data = data
        self._right = right
        self._left = left

    def __repr__(self) -> str:
        return "[Tree: head-{}, left-{}, right-{}]".format(self._data, self._right, self._left)

    def set_left(self, left: Union[int, str]):
        self._left = left

    def set_right(self, right: Union[int, str]):
        self._right = right

    def get_right(self):
        return self._right

    def get_left(self):
        return self._left


if __name__ == "__main__":
    a = Tree(data="A")
    b = Tree(data="B")
    c = Tree(data="C")
    a.set_right(b)
    a.set_left(c)
    print(a)
