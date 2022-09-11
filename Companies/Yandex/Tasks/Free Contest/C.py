n = int(input())
elements = list(map(int, input().split()))


def find_elements_n2(n, elements) -> int:
    res = 0
    for i in range(0, n):
        for j in range(i, n):
            if abs(elements[i] - elements[j]) % 200 == 0 and i<j:
                res += 1

    return res


def find_elements(n, elements) -> int:
    res = 0
    n_dict = {}
    for item in elements:
        temp = abs(item) % 200
        if temp in n_dict:
            res += n_dict[temp]
            n_dict[temp] += 1
        else:
            n_dict[temp] = 1

    return res


print(find_elements(n, elements))


# 5
# 100 200 300 23 -5

# 1
# 100