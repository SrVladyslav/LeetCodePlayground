edges_cycle = [(1, 2), (2, 3), (3, 5), (3, 4), (4, 2), (6, 7)]

edges_no_cycle = [(1, 2), (2, 3), (3, 5), (3, 4), (2, 4), (6, 7)]


from collections import defaultdict


def has_cycle_undirected_graph(edges: list[tuple[int, int]], nodes: int) -> bool:
    graph: defaultdict[int, list[int]] = defaultdict(list)

    for start, end in edges:
        graph[start].append(end)
        graph[end].append(start)

    # Check for the cycle
    visited: set[int] = set()

    def dfs(node: int, parent: int) -> bool:
        visited.add(node)

        for nei in graph[node]:
            if node == parent:
                continue  # We came from there, do not explore this branch

            if node in visited:
                return True  # We found a cycle

            return dfs(nei, node)

        return False

    for node in range(nodes):
        if node in visited:
            continue

        if dfs(node, -1):
            return True

    return False


print(f"Cycle: {has_cycle_undirected_graph(edges_cycle, 7)}")
print(f"No Cycle: {has_cycle_undirected_graph(edges_no_cycle, 7)}")
