# Задача Отрезки

# Есть произвольно задаваемый основной отрезок [A, B], и есть N - количество произвольно задаваемых доп. отрезков.
# Необходимо вычислить длину основного отрезка, на которой не происходит наложения дополнительных отрезков.

# Пример:
# A = 15, B = 165
# N1 [37, 68]
# N2 [52, 74]
# N3 [118, 146]
# N4 [35, 44]
# N5 [37, 65]
# N6 [46, 74]
#
# Ответ: 83


def count_line(A: int, B: int, N: int) -> int:
    summary_line = [i for i in range(A, B)]

    for _ in range(N):
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        for i in range(a, b):
            if i in summary_line:
                summary_line.remove(i)
    return len(summary_line)


res = count_line(15, 165, 6)
print(res)
