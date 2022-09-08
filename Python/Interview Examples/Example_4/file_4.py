# [1, 2, 2, [23, 4, [3, 2]]] -> [1, 2, 2, 23, 4, 3, 2] - пример массивов и результата
# Написать функцию, которая преобразовывает многомерный массив в одномерный(вложенность многомерного заранее неизвестна)

# идеальное решение в виде чистой функции.
def changer(array, result=None):
    if result is None:
        result = []
    for item in array:
        if isinstance(item, list):
            changer(item, result)
        else:
            result.append(item)
    return result


result = changer([1, 2, 2, [23, 4, [3, 2]]])
print(result)
