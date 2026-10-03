"""
Number of Islands
Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).

Example 1:

Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
Output: 1
Example 2:

Input: grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
Output: 4
"""

from collections import deque


def num_islands(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    visited: set[tuple[int, int]] = set()
    num_rows, num_cols = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    isles_count = 0

    def _in_bounds(row: int, col: int) -> bool:
        return (
            0 <= row < num_rows
            and 0 <= col < num_cols
            and grid[row][col] == "1"  # Is a land
        )

    def _bfs(node: tuple[int, int]) -> None:
        nonlocal visited
        nonlocal isles_count
        queue = deque([node])

        while queue:
            curr_row, curr_col = queue.popleft()
            if (curr_row, curr_col) in visited:
                continue  # We already processed it
            visited.add((curr_row, curr_col))
            for row_dir, col_dir in directions:
                new_row_dir = curr_row + row_dir
                new_col_dir = curr_col + col_dir

                if _in_bounds(new_row_dir, new_col_dir):
                    if (new_row_dir, new_col_dir) not in visited:
                        queue.append((new_row_dir, new_col_dir))

    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == "1" and (row, col) not in visited:
                _bfs(node=(row, col))
                isles_count += 1  # Each new exploration is new isle

    return isles_count


if __name__ == "__main__":
    grid = [
        ["0", "1", "1", "1", "0"],
        ["0", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    print(f"Result for grid {grid}: {num_islands(grid)}")

    grid = [
        ["1", "1", "0", "0", "1"],
        ["1", "1", "0", "0", "1"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(f"Result for grid {grid}: {num_islands(grid)}")
