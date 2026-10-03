class MultiNode:
    def __init__(self, value: int, children: list["Node"]) -> None:
        self.value = value
        self.children = children


class Node:
    def __init__(self, value: int, left: "Node" = None, right: "Node" = None) -> None:
        self.value = value
        self.left = left
        self.right = right


"""
        10
     /   |   \\
    5    15    20
   / \\         / \\
  3   8       17  25
     /\\          /
    6   9        22

        10
     /       \\
    5          20
   / \\        / \\
  3   8       17  25
     / \\         /
    6   9        22
"""
GRAPH: Node = Node(
    10,
    Node(5, Node(3, None, None), Node(8, Node(6, None, None), Node(9, None, None))),
    Node(20, Node(17, None, None), Node(value=25, left=Node(22, None, None))),
)

MULTI_GRAPH: Node = Node(
    10,
    [
        Node(5, [Node(3, []), Node(8, [Node(6, []), Node(9, [])])]),
        Node(15, []),
        Node(20, [Node(17, []), Node(25, [Node(22, [])])]),
    ],
)
EDGES: list[tuple[int, int]] = [
    (10, 5),
    (10, 15),
    (10, 20),
    (5, 3),
    (5, 8),
    (8, 6),
    (8, 9),
    (20, 17),
    (20, 25),
    (25, 22),
]
