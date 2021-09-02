class Stack:

    def __init__(self):
        self._data = []

    def __repr__(self) -> str:
        return f"Stack: {self._data}"

    def show(self):
        print(self._data)

    def push(self, num):
        self._data.append(num)

    def pop(self):
        self._data.pop()

    def length(self) -> int:
        return len(self._data)


if __name__ == "__main__":
    a = Stack() # I create my object
    a.push(10) # insert the  element
    a.show()
    a.push(23)
    a.show()
    a.push(25)
    a.show()
    a.push(27)
    a.show()
    a.push(11)
    a.show()
    print(a)
    print(a.length())
    a.push(31)
    a.pop()
    a.show()
    a.pop()
    a.show()
    a.pop()
    a.show()
    a.pop()
    a.show()
    a.pop()
    a.show()
    a.pop()
    print(a.length())
    a.show()
    print(a)
