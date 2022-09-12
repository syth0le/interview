# Поиск в глубину (Depth First Search, DFS)
""" ****** Стандартный алгоритм обхода графа в глубину. ****
1. Начните с размещения любой вершины графа на вершине стека.
2. Возьмите верхний элемент стека и добавьте его в список посещенных.
3. Создайте список смежных узлов этой вершины. Добавьте те,
 которых нет в списке посещенных, в начало стека.
4. Продолжайте повторять шаги 2 и 3, пока стек не станет пустым.
"""

GRAPH = {'A': ['B', 'C'],
         'B': ['D', 'E'],
         'C': ['F'],
         'D': [],
         'E': ['F'],
         'F': []
         }


def dfs(graph, node, visited=None):
    if visited is None:
        visited = []
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)
    return visited


print(dfs(GRAPH, 'A'))
