"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""


def findMedianSortedArraysLCSolution(nums1: list[int], nums2: list[int]) -> float:
    A = nums1
    B = nums2
    # always binary search the shorter array
    if len(A) > len(B):
        A, B = B, A

    total = len(A) + len(B)
    half = total // 2

    left = 0
    right = len(A)

    while left <= right:
        i = (left + right) // 2
        j = half - i

        Aleft = A[i - 1] if i > 0 else float("-inf")
        Aright = A[i] if i < len(A) else float("inf")

        Bleft = B[j - 1] if j > 0 else float("-inf")
        Bright = B[j] if j < len(B) else float("inf")

        # partition
        if Aleft <= Bright and Bleft <= Aright:
            # odd total length
            if total % 2 == 1:
                return min(Aright, Bright)
            # even total length
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            right = i - 1
        else:
            left = i + 1


def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:

    # Two pointers to merge the arrays, O(n)
    ptr1 = 0
    ptr2 = 0
    # This way we know when to stop
    total_length = len(nums1) + len(nums2)
    is_even = total_length % 2 == 0
    middle = total_length // 2
    curr_array = []

    while ptr1 < len(nums1) or ptr2 < len(nums2):
        # Update the pointers
        if ptr2 >= len(nums2) or (ptr1 < len(nums1) and nums1[ptr1] < nums2[ptr2]):
            curr_array.append(nums1[ptr1])
            ptr1 += 1
        else:
            curr_array.append(nums2[ptr2])
            ptr2 += 1

        if len(curr_array) == middle + 1:
            if is_even:
                return (curr_array[-1] + curr_array[-2]) / 2

            return curr_array[-1]

    return -1


if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2]
    print(
        f"\nNums1: {nums1} | Nums2: {nums2} | Median: {findMedianSortedArrays(nums1, nums2)}"
    )  # 2
    print(
        f"Nums1: {nums1} | Nums2: {nums2} | Median: {findMedianSortedArraysLCSolution(nums1, nums2)}"
    )  # 2

    nums1 = [1, 2]
    nums2 = [3, 4]
    print(
        f"\nNums1: {nums1} | Nums2: {nums2} | Median: {findMedianSortedArrays(nums1, nums2)}"
    )  # 2.5
    print(
        f"Nums1: {nums1} | Nums2: {nums2} | Median: {findMedianSortedArraysLCSolution(nums1, nums2)}"
    )  # 2.5

    nums1 = [0, 0]
    nums2 = [0, 0]
    print(
        f"\nNums1: {nums1} | Nums2: {nums2} | Median: {findMedianSortedArrays(nums1, nums2)}"
    )  # 0
    print(
        f"Nums1: {nums1} | Nums2: {nums2} | Median: {findMedianSortedArraysLCSolution(nums1, nums2)}"
    )  # 0

    nums1 = []
    nums2 = [1]
    print(
        f"\nNums1: {nums1} | Nums2: {nums2} | Median: {findMedianSortedArrays(nums1, nums2)}"
    )  # 1
    print(
        f"Nums1: {nums1} | Nums2: {nums2} | Median: {findMedianSortedArraysLCSolution(nums1, nums2)}"
    )  # 1
