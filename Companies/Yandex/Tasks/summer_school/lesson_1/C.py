# У вас есть 1000$, которую вы планируете эффективно вложить. Вам даны цены за 1000 кубометров газа за n дней.
# Можно один раз купить газ на все деньги в день i и продать его в один из последующих дней j, i < j.
# Определите номера дней для покупки и продажи газа для получения максимальной прибыли.
#
# Формат ввода
# В первой строке вводится число дней n (1 ≤ n ≤ 100000).
#
# Во второй строке вводится n чисел — цены за 1000 кубометров газа в каждый из дней. Цена — целое число от 1 до 5000.
# Дни нумеруются с единицы.
#
# Формат вывода
# Выведите два числа i и j - номера дней для покупки и продажи газа. Если прибыль получить невозможно, выведите два нуля

n = int(input())
prices = list(map(int, input().split()))


def solution(n, prices):
    hashmap = {}
    for i in range(0, n):
        for j in range(i+1, n):
            if prices[i] not in hashmap:
                hashmap[prices[i]] = (prices[j] - prices[i], prices[j])
            else:
                if hashmap[prices[i]][0] < prices[j] - prices[i]:
                    hashmap[prices[i]] = (prices[j] - prices[i], prices[j])

    result = None
    maximum = 0
    for key, value in hashmap.items():
        if value[0] > maximum:
            maximum = value[0]
            result = (key, value[1])
    if result is None:
        return f'{0} {0}'
    return f'{prices.index(result[0]) + 1} {prices.index(result[1]) + 1}'


print(solution(n, prices))
