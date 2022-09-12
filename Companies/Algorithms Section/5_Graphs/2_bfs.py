# Поиском в ширину (Breadth First Search, BFS) - Найти кратчайший путь в невзвешенном графе
# РЕШАЕТСЯ ЧЕРЕЗ ОЧЕРЕДЬ
GRAPH = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

QUEUE = []


def bfs(graph, node, visited=None):
    if visited is None:
        visited = []

    visited.append(node)
    QUEUE.append(node)

    while QUEUE:
        elem = QUEUE.pop(0)

        for neighbor in graph[elem]:
            if neighbor not in visited:
                visited.append(neighbor)
                QUEUE.append(neighbor)
    return visited


print(bfs(GRAPH, 'A', []))
print(QUEUE)
