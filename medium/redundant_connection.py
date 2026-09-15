"""
684. Redundant Connection

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""


def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    if not edges:
        return []

    if not (3 <= len(edges) <= 1000):
        return []

    nodes = len(edges)
    # DSU
    parents: list[int] = list(range(nodes + 1))
    sizes: list[int] = [1] * (nodes + 1)

    def _find(node: int) -> int:
        nonlocal parents
        while node != parents[node]:
            parents[node] = parents[parents[node]]
            node = parents[node]
        return node

    def _union(start: int, end: int) -> bool:
        nonlocal parents, sizes

        if start >= end:
            return False

        root_a = _find(start)
        root_b = _find(end)

        # If same parent, then cycle
        if root_a == root_b:
            return False

        # Start parent should be bigger
        if sizes[root_a] < sizes[root_b]:
            root_a, root_b = root_b, root_a

        parents[root_b] = root_a
        sizes[root_a] += sizes[root_b]

        return True

    # Find the edges to be removed
    result: list[int] = []

    for start, end in edges:
        if not _union(start, end):
            result = [start, end]

    return result


if __name__ == "__main__":
    print(
        f"Result for [[1,2],[2,3],[3,4],[1,4],[1,5]]: {find_redundant_connection([[1,2],[2,3],[3,4],[1,4],[1,5]])}"
    )
    print(
        f"Result for [[1,2],[2,3],[3,4],[1,4],[1,5],[2,6]]: {find_redundant_connection([[1,2],[2,3],[3,4],[1,4],[1,5],[2,6]])}"
    )
    print(
        f"Result for [[1,2],[1,3],[2,3]]: {find_redundant_connection([[1,2],[1,3],[2,3]])}"
    )
