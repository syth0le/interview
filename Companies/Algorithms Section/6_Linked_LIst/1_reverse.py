# Развернуть связный список за линейное время

class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'{self.data}'


def reverse(head: Node) -> Node:
    tail = None
    while head:
        print(head.data, end=' -> ') if head.next else print(head.data)
        head.next, tail, head = tail, head, head.next
    return tail


if __name__ == '__main__':
    head = Node(1, Node(2, Node(3, Node(4))))
    result = reverse(head)
    while result:
        print(result.data, end=' -> ') if result.next else print(result.data)
        result = result.next

