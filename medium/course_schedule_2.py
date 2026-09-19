"""
210. Course Schedule II
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
"""

from collections import deque, defaultdict


def find_order_topological_sort_lc(
    numCourses: int, prerequisites: list[list[int]]
) -> list[int]:
    graph = [[] for _ in range(numCourses)]
    for point in prerequisites:
        graph[point[1]].append(point[0])

    vis = [False] * numCourses
    path = [False] * numCourses
    res = []

    def dfs(node):
        vis[node] = True
        path[node] = True
        for neighbour in graph[node]:
            if vis[neighbour] == False:
                if dfs(neighbour):
                    return True
            elif path[neighbour]:
                return True
        path[node] = False
        res.append(node)
        return False

    for node in range(numCourses):
        if not vis[node]:
            if dfs(node):
                return []
    return res[::-1]


def find_order(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    # O(V + E)
    if not (1 <= numCourses <= 2000):
        return []

    if not (0 <= len(prerequisites) <= numCourses * (numCourses - 1)):
        return []

    courses_graph = [[] for _ in range(numCourses)]
    # indegree: dict[int, int] = {node: 0 for node in range(numCourses)}
    # indegree: dict[int, int] = dict.fromkeys(range(numCourses), 0)
    indegree: list[int] = [0] * numCourses

    for end, start in prerequisites:  # O(E)
        courses_graph[start].append(end)
        indegree[end] += 1  # Kahn approach

    # filter all the courses with indegree 0
    # queue = deque([node for node, degree in indegree.items() if degree == 0])
    queue = deque([node for node, degree in enumerate(indegree) if degree == 0])  # O(V)
    course_order: list[int] = []

    while queue:  # O(V)
        node = queue.popleft()  # Already has degree 0
        course_order.append(node)

        # explore the neighbours
        for neighbour in courses_graph[node]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)

    if len(course_order) != numCourses:
        # We have a cycle here
        return []

    return course_order


if __name__ == "__main__":
    print(
        f"Course order for numCourses = 2, prerequisites = [[1,0]]: {find_order(2, [[1, 0]])}"
    )
    print(
        f"Course order for numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]: {find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]])}"
    )
    print(f"Course order for numCourses = 1, prerequisites = []: {find_order(1, [])}")
