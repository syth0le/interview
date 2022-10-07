class Iterator:
    def __init__(self, array, cursor=0):
        self._array = array
        self._cursor = cursor - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._cursor < len(self._array) - 1:
            self._cursor += 1
            return self._array[self._cursor]
        else:
            raise StopIteration


it = Iterator([1, 2, 3, 4, 5, 1, 5, 3, 5, 3, 5], 0)
for item in it:
    print(item, end=' ')
