"""
Subsets
Given an array nums of unique integers, return all possible subsets of nums.

The solution set must not contain duplicate subsets. You may return the solution in any order.

Example 1:

Input: nums = [1,2,3]

Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [7]

Output: [[],[7]]
"""


def subsets(nums: list[int]) -> list[list[int]]:
    length = len(nums)
    result, sol = [], []

    def _backtracking(level: int) -> None:
        # Base case
        if level == length:
            result.append(sol.copy())
            return

        # Without current value
        _backtracking(level + 1)

        # Using the value
        sol.append(nums[level])
        _backtracking(level + 1)
        sol.pop()

    _backtracking(0)
    return result


print(f"Subsets for [1,2,3]: {subsets([1,2,3])}")
