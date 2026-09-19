"""
3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:

Input: nums = [0,1,1]

Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    result: list[list[int]] = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        if nums[i] > 0:
            break

        left = i + 1
        right = len(nums) - 1

        while left < right:
            suma = nums[i] + nums[left] + nums[right]
            if suma == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                # get to the next point where the numbers are not similar
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif suma < 0:
                left += 1
            else:
                right -= 1

    return result


if __name__ == "__main__":
    print(f"Result for [1,2,3]: {three_sum([1,2,3])}")
    print(f"Result for [-1,0,1,2,-1,-4]: {three_sum([-1,0,1,2,-1,-4])}")
    print(f"Result for [0,1,1]: {three_sum([0,1,1])}")
    print(f"Result for [0]: {three_sum([0])}")
