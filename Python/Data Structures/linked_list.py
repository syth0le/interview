class Node:
    def __init__(self, data=None):
        self._data = data
        self._next = None

    def set_next(self, elem):
        self._next = elem

    def get_current(self):
        return self._data, self._next


class LinkedList:

    def __init__(self):
        self._head = None

    def add(self, elem: Node):
        self._head = elem

    def __repr__(self) -> str:
        return f"Linked list: {self._head}"

    def show(self):
        next_one = self._head
        while next_one is not None:
            current, next_one = next_one.get_current()
            print(current)


if __name__ == "__main__":
    a = Node(10)
    b = Node(12)
    c = Node(14)
    a.set_next(b)
    b.set_next(c)

    linked_list = LinkedList()
    linked_list.add(a)
    print(linked_list)
    linked_list.show()

