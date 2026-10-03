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


def bfs_iterative_pre_order(root: Node) -> list[int]:
    # Pre Order: Root -> Left -> Right
    visited: list[int] = []
    queue: deque[Node] = deque([root])

    while queue:
        curr_node = queue.popleft()
        visited.append(curr_node.value)

        if curr_node.left:
            queue.append(curr_node.left)
        if curr_node.right:
            queue.append(curr_node.right)

    return visited


print(f"Pre-Order: {bfs_iterative_pre_order(GRAPH)}")


def bfs_recursive(root: Node) -> list[int]:
    result: list[int] = []

    def _bfs(level_list: list[int]) -> None:
        nonlocal result
        new_list: list[int] = []

        for item in level_list:
            result.append(item.value)

            if item.left:
                new_list.append(item.left)
            if item.right:
                new_list.append(item.right)

        if new_list:
            _bfs(new_list)

    _bfs([root])
    return result


print(f"Recursive BFS: {bfs_recursive(GRAPH)}")
