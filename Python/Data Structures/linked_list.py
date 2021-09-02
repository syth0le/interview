class Node:
    def __init__(self, data=None):
        self._data = data
        self._next = None

    def set_next(self, elem):
        self._next = elem

    def get_current(self):
        return self._data, self._next

    def delete(self, prev):
        prev.set_next(self.get_current()[1])


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
            yield current, next_one
            # return current, next_one


if __name__ == "__main__":
    a = Node(4)
    b = Node(5)
    c = Node(1)
    d = Node(9)
    a.set_next(b)
    b.set_next(c)
    c.set_next(d)

    linked_list = LinkedList()
    linked_list.add(a)
    for elem, next_el in linked_list.show():
        print(elem, next_el)

    b.delete(a)

    linked_list = LinkedList()
    linked_list.add(a)
    print(linked_list)
    for elem, next_el in linked_list.show():
        print(elem, next_el)



