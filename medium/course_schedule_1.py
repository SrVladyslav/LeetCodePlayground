"""
207. Course Schedule
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi]
indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""

from collections import deque


def course_schedule(numCourses: int, prerequisites: list[list[int]]) -> bool:
    if not (1 <= numCourses <= 1000):
        return False

    if not (0 <= len(prerequisites) <= numCourses * (numCourses - 1)):
        return False

    # O(V + E)
    graph: list[list[int]] = [[] for _ in range(numCourses)]
    indegree: list[int] = [0] * numCourses
    for end, start in prerequisites:
        indegree[end] += 1
        graph[start].append(end)

    # -1: not visited, 0: visiting, 1: visited
    state: list[int] = [-1] * numCourses
    result: list[int] = []

    def _dfs(node: int) -> bool:
        stack: list[int, bool] = [(node, True)]

        while stack:
            node, processed = stack.pop()

            if processed:
                state[node] = 1
                result.append(node)  # Processed, since this is his on return way
                continue

            if state[node] == 0:  # Cycle, since we are on the node while visiting
                return False  # We cant finish them

            if state[node] == 2:  # Already processed, forget this node
                continue

            state[node] = 0  # Start visiting the node
            stack.append((node, True))

            for neighbour in graph[node]:
                if state[neighbour] == 0:  # Visiting, so cycle
                    return False

                if state[neighbour] == -1:  # Not visited, so visit it
                    stack.append((neighbour, False))

    for node in range(numCourses):
        # Already visited and investigated
        if state[node] != -1:
            continue

        res = _dfs(node)

    if len(result) != numCourses:
        return False

    return True


def can_finish_with_kahn(numCourses: int, prerequisites: list[list[int]]) -> bool:
    if not (1 <= numCourses <= 2000) or not (0 <= len(prerequisites) <= 5000):
        return False

    # The courses go from 0 to last, so if no prerequisites, they should finish correctly
    if len(prerequisites) == 0:
        return True

    # Approach with the Kahn algoritm by deleting the in-degree
    graph: list[list[int]] = [[] for _ in range(numCourses)]
    indegree: list[int] = [0] * numCourses

    for last, first in prerequisites:
        graph[first].append(last)
        indegree[last] += 1

    # Process the degrees in order to have the correct order
    order: list[int] = []
    # queue = deque([node for node, degree in enumerate(range(numCourses)) if degree == 0])
    queue = deque([node for node in range(numCourses) if indegree[node] == 0])

    while queue:
        node = queue.popleft()
        # The in-degree is 0
        order.append(node)

        # Explore its deendencies
        for neighbour in graph[node]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)

    if numCourses != len(order):
        return False  # It has a cycle, so it is impossible to end

    return True


if __name__ == "__main__":
    print(
        f"Course order for numCourses = 2, prerequisites = [[1,0]]: {course_schedule(2, [[1, 0]])}"
    )  # True
    print(
        f"Course order for numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]: {course_schedule(4, [[1, 0], [2, 0], [3, 1], [3, 2]])}"
    )
    print(
        f"Course order for numCourses = 2, prerequisites = [[1,0],[0,1]]: {course_schedule(2, [[1,0],[0,1]])}"
    )  # False

    # Kahn implementation

    print(
        f"Course order for numCourses = 2, prerequisites = [[1,0]]: {can_finish_with_kahn(2, [[1, 0]])}"
    )  # True
    print(
        f"Course order for numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]: {can_finish_with_kahn(4, [[1, 0], [2, 0], [3, 1], [3, 2]])}"
    )
    print(
        f"Course order for numCourses = 2, prerequisites = [[1,0],[0,1]]: {can_finish_with_kahn(2, [[1,0],[0,1]])}"
    )  # False
