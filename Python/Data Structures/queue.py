class Queue:

    def __init__(self):
        self._data = []

    def __repr__(self) -> str:
        return f"Queue: {self._data}"

    def show(self) -> None:
        print(self._data)

    def enque(self, num):
        self._data.append(num)

    def deque(self):
        self._data.pop(0)

    def length(self) -> int:
        return len(self._data)


if __name__ == "__main__":
    b = Queue()
    b.enque(2)  # put the element into the queue
    b.enque(3)
    b.enque(4)
    b.enque(5)
    b.show()
    print(b)
    b.deque()  # # remove the first element that we have put in the queue
    b.show()
    print(b)
