"""
Burst Balloons
You are given an array of integers nums of size n. The ith element represents a balloon with an integer value of nums[i]. You must burst all of the balloons.

If you burst the ith balloon, you will receive nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then assume the out of bounds value is 1.

Return the maximum number of coins you can receive by bursting all of the balloons.

Example 1:

Input: nums = [4,2,3,7]

Output: 143

Explanation:
nums = [4,2,3,7] --> [4,3,7] --> [4,7] --> [7] --> []
coins =  4*2*3    +   4*3*7   +  1*4*7  + 1*7*1 = 143

"""


class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        # Add virtual balloons at both ends
        nums = [1] + nums + [1]

        # dp[(left, right)] = maximum coins
        # obtainable by bursting balloons strictly
        # between left and right
        dp: dict[tuple[int, int], int] = {}

        def backtrack(left: int, right: int) -> int:
            # No balloons between left and right
            if left + 1 == right:
                return 0

            # Memoization
            if (left, right) in dp:
                return dp[(left, right)]

            max_coins = 0

            # Choose which balloon is burst LAST
            for i in range(left + 1, right):
                current_coins = nums[left] * nums[i] * nums[right]

                left_coins = backtrack(left, i)
                right_coins = backtrack(i, right)

                total_coins = left_coins + current_coins + right_coins

                max_coins = max(max_coins, total_coins)

            dp[(left, right)] = max_coins
            return max_coins

        return backtrack(0, len(nums) - 1)
