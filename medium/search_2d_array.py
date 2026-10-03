"""
Search a 2D Matrix
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1:



Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

Output: true
Example 2:



Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

Output: false
"""


def search_2d_array(matrix: list[list[int]], target: int) -> bool:
    if not target:
        return False

    def _find_row(array: list[int], target: int) -> int:
        left, right = 0, len(array) - 1

        while left <= right:  # We need the indices to overlap to know row
            if array[right] == target:
                return right

            if array[right] > target:
                right -= 1
            else:
                left += 1

        return right  # Since left == right if all is explored

    def _item_inside(array: list[int], target: int) -> bool:
        left, right = 0, len(array) - 1

        while left <= right:  # We need the indices to overlap to know row
            if array[left] == target:
                return True

            if array[left] < target:
                left += 1
            else:
                right -= 1

        return False

    first_col: list[int] = [row[0] for row in matrix]  # O(n)
    row = _find_row(array=first_col, target=target)
    return _item_inside(matrix[row], target)


matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
target = 10
print(f"For value {matrix} and tg {target}: {search_2d_array(matrix, target)}")
print(f"For value {matrix} and tg {9}: {search_2d_array(matrix, 9)}")
