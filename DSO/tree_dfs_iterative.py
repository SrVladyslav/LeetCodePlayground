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


def dfs_iterative_pre_order(root: Node) -> list[int]:
    result: list[int] = []
    stack: list[Node] = [root]

    # We want the typical DFS, Root -> Left -> Right
    # So we push in reverse order since this is LIFO
    # Right -> Left -> Root

    while stack:
        top = stack.pop()

        if top.right:
            stack.append(top.right)

        if top.left:
            stack.append(top.left)

        result.append(top.value)

    return result


def dfs_iterative_inorder(root: Node) -> list[int]:
    result: list[int] = []
    stack: list[Node] = [(root, False)]  # (Node, processed)

    while stack:
        node, processed = stack.pop()

        if processed:
            result.append(node.value)
            continue

        # We want Left -> Root -> Right
        # We push in reverse order since this is LIFO
        # Right -> Root -> Left
        if node.right:
            stack.append((node.right, False))

        stack.append((node, True))

        if node.left:
            stack.append((node.left, False))

    return result


def dfs_iterative_post_order(root: Node) -> list[int]:
    result: list[int] = []
    stack: list[tuple[Node, bool]] = [(root, False)]

    while stack:
        node, processed = stack.pop()

        if processed:
            result.append(node.value)
            continue

        # If desired is Left -> Right -> Root
        # Then push in reverse since this is LIFO
        # Root -> Right -> Left
        stack.append((node, True))

        if node.right:
            stack.append((node.right, False))

        if node.left:
            stack.append((node.left, False))

    return result


print("Pre Order Iterative DFS: ", dfs_iterative_pre_order(GRAPH))
print(f"Inorder Iterative DFS: {dfs_iterative_inorder(GRAPH)}")
print(f"Post Order Iterative DFS: {dfs_iterative_post_order(GRAPH)}")
