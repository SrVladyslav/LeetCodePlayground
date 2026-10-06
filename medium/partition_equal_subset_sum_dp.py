"""
416. Partition Equal Subset Sum
Solved
Medium
Topics
premium lock icon
Companies
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.



Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        length = len(nums)
        nums_sum = sum(nums)

        # If the number is not divisible by 2, isinvalid
        if nums_sum & 1 == 1:
            return False

        if not (1 <= len(nums) <= 200):
            return False

        remaining = nums_sum >> 1

        # State dp[i][j]: represents the max possible subset up to j using number i
        dp = [[0] * (remaining + 1) for _ in range(length + 1)]
        # Base case: all zeros in first row and column.

        for row in range(1, length + 1):
            curr_val = nums[row - 1]
            for col in range(1, remaining + 1):
                # Skip the number and we don't take it
                dp[row][col] = dp[row - 1][col]

                # We take the number at row position.
                if curr_val <= col:
                    dp[row][col] = max(
                        dp[row][col],
                        curr_val
                        + dp[row - 1][
                            col - curr_val
                        ],  # We wanna reuse the best of the skipped and remaining value
                    )

        return dp[-1][-1] == remaining


if __name__ == "__main__":
    sol = Solution()

    print(f"TRUE: [1,5,11,5]: {sol.canPartition([1,5,11,5])}")
    print(f"TRUE: [1,5,10,1,5]: {sol.canPartition([1,5,10, 1,5])}")
    print(f"FALSE: [1,2,3,5]: {sol.canPartition([1,2,3,5])}")
