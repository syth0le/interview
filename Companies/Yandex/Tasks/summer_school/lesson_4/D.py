# Дано неориентированное дерево, подвешенное за вершину 1. Для каждой вершины подсчитайте, сколько вершин содержится в поддереве, подвешенном за данную вершину.
#
# Формат ввода
# В первой строке вводится число V — количество вершин (3 ≤ V ≤ 100000)
#
# В следующих V-1 строках записано по два числа: номера соединенных ребром вершин
#
# Формат вывода
# Выведите V чисел — размеры поддеревьев для каждой из вершин
#
# Пример 1
# Ввод	Вывод
# 4
# 1 2
# 1 3
# 1 4
# 4 1 1 1
# Пример 2
# Ввод	Вывод
# 7
# 1 2
# 1 3
# 1 4
# 5 1
# 5 6
# 5 7
import sys

sys.setrecursionlimit(1000000)
V = int(input())

GRAPH = {}
RESULT = {}
for _ in range(V-1):
    v_1, v_2 = list(map(int, input().split()))
    RESULT[v_1] = 0
    RESULT[v_2] = 0
    if v_1 > v_2:
        if v_2 in GRAPH:
            GRAPH[v_2].add(v_1)
            GRAPH[v_1] = set()
        else:
            GRAPH[v_2] = {v_1}
            GRAPH[v_1] = set()
    else:
        if v_1 in GRAPH:
            GRAPH[v_1].add(v_2)
            GRAPH[v_2] = set()
        else:
            GRAPH[v_1] = {v_2}
            GRAPH[v_2] = set()


def dfs(graph, node, visited):
    temp = 0
    if node not in visited:
        visited.append(node)
        temp += len(graph[node])
        for neighbor in graph[node]:
            temp += dfs(graph, neighbor, visited)
        RESULT[node] += temp
    return temp


print(GRAPH)
dfs(GRAPH, 1, [])
print(*[RESULT[i]+1 for i in RESULT])
