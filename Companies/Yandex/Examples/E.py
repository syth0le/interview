# Дано бинарное дерево со взвешенными узлами
# Найти ветку с максимальной суммой узлов

class Node:
    def __init__(self, val):
        self.left = None
        self.val = val
        self.right = None


def finder(node: Node):
    current = node.val
    left = None
    right = None
    if node.left:
        left = finder(node.left)
        if node.right is None:
            current += left
    if node.right:
        right = finder(node.right)
        if node.left is None:
            current += right
    if right and left:
        current += right if right > left else left
    return current


root = Node(13)
left = Node(12)
right = Node(14)
root.left = left
root.right = right
left.left = Node(20)
left.right = Node(1)
right.right = Node(21)

#      21
#     /
#    14
#   /
# 13   1
#   \ /
#    12
#     \
#      20
print(finder(root))  # 48 (13 + 14 + 21)
