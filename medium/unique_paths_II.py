"""
63. Unique Paths II
Solved
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        """
        What happen if we have an obstacle right and on bottom of the ini point?

        This is a typoical GRID DP problem
        """
        if not obstacleGrid:
            return 0

        # State: unique paths, we will also have a dp grid
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [[0] * (cols + 1)] * (rows + 1)
        # Base case
        dp[1][1] = 1

        # General case
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                dp[row][col] = (
                    dp[row - 1][col] + dp[row][col - 1]
                    if obstacleGrid[row - 1][col - 1] == 0
                    else 0
                )

        return dp[row][col]


if __name__ == "__main__":
    solution = Solution()
    print(solution.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(solution.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 1], [0, 0, 0]]))
    print(solution.uniquePathsWithObstacles([[1, 0, 0], [0, 1, 1], [0, 0, 0]]))
    print(solution.uniquePathsWithObstacles([[0, 1, 0], [1, 0, 0], [0, 0, 0]]))
    print(solution.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 1], [0, 1, 0]]))
