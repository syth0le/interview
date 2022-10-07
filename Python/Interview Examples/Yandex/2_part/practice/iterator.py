class Iterator:
    def __init__(self, array, cursor):
        self._array = array
        self._cursor = cursor

    def __iter__(self):
        return self

    def __next__(self):
        if self._cursor < len(self._array):
            self._cursor += 1
            return 1
        else:
            raise StopIteration
