# Есть две поисковые выдачи, которые заданы векторами простых чисел длины N,
# для всех K от 1 до N нужно посчитать количество общих документов в топах размера K.
# Задача про пересечение топов двух выдач
# Для
# А = [1,3,5,6,7]
# Когда К = 3
# Топ равен 1, 3, 5

V1 = [1, 2, 3, 4, 5]
V2 = [2, 3, 5, 6, 7]


def solution(num1: list[int], num2: list[int]):
    N = len(num1)
    hashmap = {}
    res = []
    for i in range(1, N + 1):
        curr = num1[i-1]
        if curr not in hashmap:
            hashmap[curr] = 1
        else:
            hashmap[curr] += 1
        temp = 0
        for item in num2[:i]:
            if item in hashmap:
                temp += 1
        res.append(temp)
    return res


print(solution(V1, V2))
