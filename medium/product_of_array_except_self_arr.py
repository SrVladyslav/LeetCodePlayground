"""
Products of Array Except Self
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        total_prod: int = 1
        zero_count: int = 0

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total_prod *= num

        print(total_prod)

        output: list = []
        for num in nums:

            if zero_count >= 2:
                output.append(0)

            elif zero_count == 1:
                output.append(total_prod if num == 0 else 0)

            else:
                output.append(total_prod // num)

        return output
