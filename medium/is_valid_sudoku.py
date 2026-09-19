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

from collections import defaultdict


def is_valid_sudoku(board: list[list[str]]) -> bool:
    quadrant_sets = defaultdict(set[int])  # (row%3, col%3) = {nums}
    rows_set: set[int] = set()
    cols_set = defaultdict(set[int])

    for row in range(len(board)):
        rows_set = set()
        for col in range(len(board)):
            # Inner quadrant
            i_row = row // 3
            i_col = col // 3
            curr_value = board[row][col]
            is_digit = curr_value.isdigit()
            if curr_value in quadrant_sets[(i_row, i_col)]:
                return False
            elif is_digit:
                quadrant_sets[(i_row, i_col)].add(curr_value)

            # Rows and cols
            if curr_value in rows_set:
                return False
            elif is_digit:
                rows_set.add(curr_value)

            # Cols
            if curr_value in cols_set[col]:
                return False
            elif is_digit:
                cols_set[col].add(curr_value)

    return True


board = [
    [".", ".", "4", ".", ".", ".", "6", "3", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["5", ".", ".", ".", ".", ".", ".", "9", "."],
    [".", ".", ".", "5", "6", ".", ".", ".", "."],
    ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
    [".", ".", ".", "7", ".", ".", ".", ".", "."],
    [".", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
]
board1 = [
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", "1", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
board2 = [
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
if __name__ == "__main__":
    print(is_valid_sudoku(board))  # False
    print(is_valid_sudoku(board1))  # False
    print(is_valid_sudoku(board2))  # True
