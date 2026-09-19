"""
Longest Consecutive Sequence
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
"""


def longest_consecutive_sequence(nums: list[int]) -> int:
    if not nums:
        return 0

    num_to_idx: dict[int, int] = {}
    parent = list(range(len(nums)))
    sizes = [1] * len(nums)

    def _find(node: int) -> int:
        while node != parent[node]:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    def _union(a: int, b: int) -> None:
        root_a = _find(a)
        root_b = _find(b)

        if root_a == root_b:
            return None

        if sizes[root_a] < sizes[root_b]:
            root_a, root_b = root_b, root_a

        parent[root_b] = root_a
        sizes[root_a] += sizes[root_b]

    # Explore all possibilities
    for idx, num in enumerate(nums):
        if num in num_to_idx:
            continue

        num_to_idx[num] = idx

        if num - 1 in num_to_idx:
            _union(
                idx, num_to_idx[num - 1]
            )  # Since we know the number previous to current, we connects their indices inthe DSU graph., and update sizes

        if num + 1 in num_to_idx:
            _union(idx, num_to_idx[num + 1])

    return max(sizes)


if __name__ == "__main__":
    print(
        f"LCS for [2,20,4,10,3,4,5]: {longest_consecutive_sequence([2,20,4,10,3,4,5])}"
    )
    print(
        f"LCS for [0,3,2,5,4,6,1,1]: {longest_consecutive_sequence([0,3,2,5,4,6,1,1])}"
    )
