# Вася занимается строительством лесенок из блоков. Лесенка состоит из ступенек, при этом i-ая ступенька должна состоять
# ровно из i блоков. По заданному числу блоков n определите максимальное количество ступенек в лесенке, которую можно
# построить из этих блоков.
#
# Формат ввода
# Вводится одно число n (1 ≤ n ≤ 231 - 1).
#
# Формат вывода
# Выведите одно число — количество ступенек в лесенке.

N = int(input())


def solution(n):
    accum = 0
    i = 1
    while accum <= n:
        if accum + i > n:
            break
        accum += i
        i += 1
    return i - 1


print(solution(N))
