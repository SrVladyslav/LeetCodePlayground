"""
685. Redundant Connection II
In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.
The given input is a directed graph that started as a rooted tree with n nodes (with distinct values from 1 to n), with one additional directed edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [ui, vi] that represents a directed edge connecting nodes ui and vi, where ui is a parent of child vi.
Return an edge that can be removed so that the resulting graph is a rooted tree of n nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

Example 1:

Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:

Input: edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
Output: [4,1]

1) All the nodes passed can fit perfectly in the memory? YES
2) Can we hve inverse edges, like a -> b and b->a? NO
3) How many nodes we have? like len(edges), or how? And every node is different I suppose.
4) Since every node has exactly one parent, exep the root, therefore we have one component
from collections import defaultdict
"""


def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    if not edges:
        return []

    if not (3 <= len(edges) <= 1000):
        return []

    nodes = len(edges) + 1

    # This approach is about a tree-like graph + one extra edge, so we can use DSU for cycle searching if we findthe
    # probable extra edge.

    # Step 1: Find the indegree > 1 of the nodes, basically a node with multiple parents, we need to remove it and check for cycles.
    indegree: list[int] = [0] * nodes
    # Save the two possible edges of parents
    first_edge: list[int] = []
    second_edge: list[int] = []
    for start, end in edges:
        if indegree[
            end
        ]:  # Means that we already have one degree there, so this is in-degree > 1 = extra parent
            first_edge = [indegree[end], end]
            second_edge = [start, end]
        else:
            indegree[end] = start

    # Step 2: Once edge removed, we can apply a simple DSU aproximation to find the cycle.
    parents: list[int] = list(range(nodes))
    size: list[int] = [1] * nodes

    def _find(node: int) -> int:
        while node != parents[node]:
            # Here we are flattening and combining the parents, so we can use an optimized DSU O(V + E)
            parents[node] = parents[parents[node]]
            node = parents[node]
        return node

    def _union(start: int, end: int) -> bool:
        # First obtain the roots for each node, so we can obtain if they are the same node or not
        root_a = _find(start)
        root_b = _find(end)

        # If they are the same, then we have a cycle
        if root_a == root_b:
            return False

        # If they are not, then we should update the nodes with the parents
        if size[root_a] < size[root_b]:
            root_a, root_b = root_b, root_a

        # Update the sizes and the parent, parent_a is the biggest tree in here
        parents[root_b] = (
            root_a  # So the smaller tree should point to the bigger root_a
        )
        size[root_a] += size[root_b]  # And now the sizes should be added
        return True

    # Ok, now, let's check for a cycle in the graph when the last second edge is not present, so jump it
    for start, end in edges:
        if second_edge and second_edge == [start, end]:
            continue  # Just skip it as it was not present in here

        if not _union(start, end):
            # If we still have a cycle, then is the first edge or the current on eif first is not present, which is the same
            return first_edge if first_edge else [start, end]

    # Stage 3: Finally if any edge is present, then we should return the second, which was the correct guess
    return second_edge


if __name__ == "__main__":
    print(
        f"Result for [[1,2],[1,3],[2,3]]: {find_redundant_connection([[1,2],[1,3],[2,3]])}"
    )  # [2,3]
    print(
        f"Result for [[1,2],[2,3],[3,4],[4,1],[1,5]]: {find_redundant_connection([[1,2],[2,3],[3,4],[4,1],[1,5]])}"
    )  # [4,1]
