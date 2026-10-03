"""
Minimum Size Subarray Sum
You are given an array of positive integers nums and a positive integer target,

return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

- Return the smallest subsrray with a sum greater or equal to target.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: target = 10, nums = [2,1,5,1,5,3]
14 -> 12 -> 11 ->
Output: 3
Explanation: The subarray [5,1,5] has the minimal length under the problem constraint.

Time: O(n^2)

Time: O(n)


"""


def min_sub_array_len_binary_search(
    target: int, nums: list[int]
) -> int:  # t: O(n log n) s: O(n)
    max_prefix_sum_ptr: int = len(nums) + 1
    prefix_sum = [0] * (len(nums) + 1)

    def bisect_left(arr: list[int], target: int) -> int:
        left, right = 0, len(arr)

        while left < right:
            middle = left + (right - left) // 2
            if arr[middle] < target:
                left = middle + 1
            else:
                right = middle
        return left

    for idx, num in enumerate(nums):  # O(n)
        prefix_sum[idx + 1] = prefix_sum[idx] + num

    for idx, num in enumerate(prefix_sum):  # O(n)
        needed = target + num
        curr_left = bisect_left(prefix_sum, needed)
        if curr_left <= len(nums):
            max_prefix_sum_ptr = min(max_prefix_sum_ptr, curr_left - idx)

    return max_prefix_sum_ptr if max_prefix_sum_ptr < len(nums) else 0


def min_sub_array_len_pointers(target: int, nums: list[int]) -> int:
    if not nums:
        return 0
    if target <= 0:
        return 0

    slow = 0
    min_sub_array_len = len(nums) + 1
    curr_sum_window = 0

    for fast in range(len(nums)):
        curr_sum_window += nums[fast]

        while slow <= fast and curr_sum_window >= target:
            min_sub_array_len = min(min_sub_array_len, fast - slow + 1)
            curr_sum_window -= nums[slow]
            slow += 1

    return min_sub_array_len if min_sub_array_len < len(nums) + 1 else 0


print(min_sub_array_len_binary_search(10, [2, 1, 5, 1, 5, 3]))
print(min_sub_array_len_pointers(10, [2, 1, 5, 1, 5, 3]))
