V1 = [1, 2, 3, 9, 8, 4, 5]
V2 = [2, 3, 5, 6, 7, 8, 9]


def add_to_hashmap(v, hashmap):
    if v not in hashmap:
        hashmap[v] = 1
    else:
        hashmap[v] += 1


def solution(num1: list[int], num2: list[int]):
    N = len(num1)
    hashmap1 = {}
    hashmap2 = {}
    res = []
    prev1 = prev2 = 0
    for i in range(1, N + 1):
        curr1 = num1[i-1]
        curr2 = num2[i-1]
        add_to_hashmap(curr1, hashmap1)
        add_to_hashmap(curr2, hashmap2)
        if curr1 in hashmap2:
            prev1 += 1
        if curr2 in hashmap1:
            prev2 += 1
        # print(prev1, prev2)
        res.append(prev1 + prev2)
    return res


print(solution(V1, V2))
