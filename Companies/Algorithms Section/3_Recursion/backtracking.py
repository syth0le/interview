# Поиск с возвратом
# Это метод решения задач, где требуется перебор вариантов.

# Рассмотрим задачу: дано число N, нужно сгенерировать все правильные скобочные последовательности из
# N открывающих и N закрывающих скобок.

N = 2
# https://hashsum.ru/generaciya-skobochnyx-posledovatelnostej/
# n = 1 ()
# n = 2 ()() (())
# n = 3 ()()() (())() ()(()) ((())) (()())


def backtracking(n: int):

    def wrapper(n, s, left, right):
        if left == n and right == n:
            print(s)
        else:
            if left < n:
                wrapper(n, s+'(', left+1, right)
            if right < left:
                wrapper(n, s+')', left, right+1)

    wrapper(n, '', 0, 0)


backtracking(N)
