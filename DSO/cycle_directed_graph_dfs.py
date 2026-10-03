edges_cycle = [(1, 2), (2, 3), (3, 5), (3, 4), (4, 2), (6, 7)]

edges_no_cycle = [(1, 2), (2, 3), (3, 5), (3, 4), (2, 4), (6, 7)]


def has_cycle_directed_graph(edges: list[tuple[int, int]], nodes: int) -> bool:
    graph = [[] for _ in range(nodes + 1)]

    for start, end in edges:
        graph[start].append(end)

    # Now check for the cycle
    state: list[int] = [0] * (
        nodes + 1
    )  # States are  0: unvisited, 1: VISITING, 2: VISITED

    def dfs(node: int) -> bool:
        if state[node] == 2:
            return False  # We already explored that path

        if state[node] == 1:
            return True  # We have a cycle in here, since we still visiting the nodes

        state[node] = (
            1  # So, we set i t as an exploring state since we are explring the node
        )

        for neighbour in graph[node]:
            if dfs(neighbour):
                return True

        # Here we already explored the node, so mark it as an explored one
        state[node] = 2

        return False

    for node in range(nodes):
        if state[node] == 0 and dfs(node):
            return True

    return False


print(f"Cycle: {has_cycle_directed_graph(edges_cycle, 7)}")
print(f"No Cycle: {has_cycle_directed_graph(edges_no_cycle, 7)}")


edges_cycle = [(1, 2), (2, 3), (3, 5), (3, 4), (4, 2), (6, 7)]

edges_no_cycle = [(1, 2), (2, 3), (3, 5), (3, 4), (2, 4), (6, 7)]


def has_cycle_directed(edges: list[tuple[int, int]], nodes: int) -> bool:
    # Using kahn algorithm
    from collections import deque

    graph = [[] for _ in range(nodes + 1)]
    indegree = [0] * (nodes + 1)

    for start, end in edges:
        graph[start].append(end)
        indegree[end] += 1

    # Nos start processing Kahn algorithm
    queue = deque([node for node in range(1, nodes) if indegree[node] == 0])
    processed_nodes: int = 0

    while queue:
        node = queue.popleft()
        processed_nodes += 1  # Every node out, is one processed

        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)

    return (
        processed_nodes != nodes
    )  # There is a cycle if processed nodes are not equal i number to the normal ones


print(has_cycle_directed(edges_cycle, 7))
print(has_cycle_directed(edges_no_cycle, 7))
