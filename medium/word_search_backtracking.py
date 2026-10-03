"""
Word Search
Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

Example 1:



Input:
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "CAT"

Output: true
Example 2:



Input:
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "BAT"

Output: false
"""


def exist(board: list[list[str]], word: str) -> bool:
    if not board:
        return False
    if len(word) == 0:
        return False

    num_rows = len(board)
    num_cols = len(board[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited: set[tuple[int, int]] = set()

    def dfs(row: int, col: int, remaining: str) -> bool:
        # Base case
        if len(remaining) == 0:
            return True

        # Use the new letter
        children_responses = False
        for dir_row, dir_col in directions:
            new_row = row + dir_row
            new_col = col + dir_col
            if not (0 <= new_row < num_rows and 0 <= new_col < num_cols):
                continue

            # Prune the path
            if board[new_row][new_col] != remaining[0]:
                continue

            if (new_row, new_col) not in visited:
                # Explore new path
                visited.add((new_row, new_col))
                if dfs(new_row, new_col, remaining[1:]):
                    children_responses = True
                # Undo the path
                visited.remove((new_row, new_col))

        return children_responses

    for row in range(num_rows):
        for col in range(num_cols):
            if board[row][col] != word[0]:
                continue

            visited.add((row, col))
            if dfs(row, col, word[1:]):
                return True

            visited.remove((row, col))

    return False


if __name__ == "__main__":
    board = [
        ["A", "B", "C", "D"],
        ["S", "A", "A", "T"],
        ["A", "C", "A", "E"],
    ]
    word = "CAT"
    print(f"Result for {board} and {word}: {exist(board, word)}")

    board = [
        ["A", "B", "C", "D"],
        ["S", "A", "A", "T"],
        ["A", "C", "A", "E"],
    ]
    word = "BAT"
    print(f"Result for {board} and {word}: {exist(board, word)}")
