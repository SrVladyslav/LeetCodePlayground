"""
We have nums which is an array of different numbers, and a target, which is the number we should find as the sum of the nums of the array, we can do basically + or - before each one of the numbers

eg: nums = [1,1,1,1,1] target= 3  -> output= 5
"""


def findTargetSumWays(nums: list[int], target: int) -> int:
    dp: dict[tuple[int, int], int] = {}

    def backtracking(index: int, total: int) -> int:
        # Base case
        if index >= len(nums):
            return 1 if total == target else 0

        if (index, total) in dp:
            return dp[(index, total)]

        dp[(index, total)] = 0

        # We need to sum the values
        dp[(index, total)] += backtracking(index + 1, total + nums[index])

        # We need to remove the value
        dp[(index, total)] += backtracking(index + 1, total - nums[index])

        return dp[(index, total)]

    return backtracking(0, 0)


print(findTargetSumWays([1, 1, 1, 1, 1], 3))
