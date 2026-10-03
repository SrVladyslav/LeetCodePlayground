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


def bfs_recursive(root: Node) -> list[int]:
    if not root:
        return []

    result: list[int] = []

    def _bfs(nodes: list[Node]) -> None:
        nonlocal result

        net_level: list[Node] = []

        for node in nodes:
            result.append(node.value)

            if node.left:
                net_level.append(node.left)
            if node.right:
                net_level.append(node.right)

        if net_level:
            _bfs(net_level)

    _bfs([root])
    return result


print(f"Recursive BFS: {bfs_recursive(GRAPH)}")
