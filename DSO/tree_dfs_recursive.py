from collections import deque
from base_node import Node, GRAPH, EDGES

"""
        10
     /       \\
    5         20
   / \\        / \\
  3   8       17  25
     / \\         /
    6   9        22
"""


def dfs_recursive(root: Node) -> list[int]:
    def _dfs(node: int) -> list[int]:
        # Pre-Order
        visited: list[int] = [node.value]

        if node.left:
            visited += _dfs(node.left)

        # In-Order
        # visited: list[int] = [node.value]

        if node.right:
            visited += _dfs(node.right)

        # Post-Order
        # visited: list[int] = [node.value]

        return visited

    return _dfs(root)


res = dfs_recursive(GRAPH)
print(res)
