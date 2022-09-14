# На прямой расположены стойла, в которые необходимо расставить коров так, чтобы минимальное расcтояние между коровами
# было как можно больше.
#
# Формат ввода
# В первой строке вводятся числа N (2 < N < 10001) – количество стойл и K (1 < K < N) – количество коров.
# Во второй строке задаются N натуральных чисел в порядке возрастания – координаты стойл (координаты не превосходят 109)
#
# Формат вывода
# Выведите одно число – наибольшее возможное допустимое расстояние.

n, k = list(map(int, input().split()))
stays = list(map(int, input().split()))


def solution(stays, n, k):
    def check(num, k, stays):
        accum = 1
        prev = stays[0]
        for i in range(len(stays)):
            if stays[i] - prev >= num:
                accum += 1
                prev = stays[i]
        return accum >= k

    left = 0
    right = stays[-1]
    while left < right:
        mid = (left + right + 1) // 2
        if check(mid, k, stays):
            left = mid
        else:
            right = mid - 1
    return left


print(solution(stays, n, k))
