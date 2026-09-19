"""
Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
"""

from collections import defaultdict
from heapq import heappush, heappop


def top_k_frequent_n_log_n(nums: list[int], k: int) -> list[int]:
    counter = defaultdict(int)

    for curr_num in nums:
        counter[curr_num] += 1

    n = [(count, num) for num, count in counter.items()]
    n.sort(key=lambda x: -x[0])

    return [i for _, i in n[:k]]


def bucket_sort(nums: list[int], k: int) -> list[int]:
    counter = defaultdict(int)

    for curr_num in nums:
        counter[curr_num] += 1

    # Bucket sort
    bucket_freq: list[list[int]] = [[] for _ in range(len(nums) + 1)]

    for number, count in counter.items():
        bucket_freq[count].append(number)

    result: list[int] = []
    for i in range(len(bucket_freq) - 1, 0, -1):
        for number in bucket_freq[i]:
            if len(result) < k:
                result.append(number)
            else:
                return result

    return result
