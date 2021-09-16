class A:
    def __init__(self, *args):
        self.arr = args


def unique(arr, cls) -> list:
    temp = []
    temp.append(arr[0])
    for elem in arr:
        print(elem.arr)
        for i in temp:
            print(i.arr)
            if not elem.arr == i.arr:
                temp.append(elem)
    return temp


if __name__ == "__main__":
    smth = [A(1, "ab"), A(2, "ab"), A(2, "aa"), A(1, "ab")]
    print(unique(smth, A()))