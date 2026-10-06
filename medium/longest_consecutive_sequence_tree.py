class Node:
    def __init__(self, value: int, left: "Node" = None, right: "Node" = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def longest_consecutive_sequence(root: Node) -> int:
    if not root:
        return 0

    max_sequence: int = 0

    def dfs(curr_node: Node, curr_sequence: int, previous_value: int = None) -> bool:
        nonlocal max_sequence

        if curr_node is None:
            return 0

        if previous_value is not None and curr_node.value == previous_value + 1:
            curr_sequence += 1
        else:
            curr_sequence = 1

        max_sequence = max(max_sequence, curr_sequence)

        dfs(curr_node.left, curr_sequence, curr_node.value)
        dfs(curr_node.right, curr_sequence, curr_node.value)

    dfs(root, 0, root.value - 1)
    return max_sequence


if __name__ == "__main__":
    TREE_1: Node = Node(
        5,
        Node(6, None, None),
        Node(1, Node(2, None, Node(3, None, None)), Node(7, None, None)),
    )

    print(f"Longest sequence for TREE 1: {longest_consecutive_sequence(TREE_1)}")
