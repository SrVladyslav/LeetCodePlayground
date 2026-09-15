import random
from collections import deque
from typing import Generator
from pprint import pprint


class Minesweeper:
    MINE: int = 9

    def __init__(self, rows: int, cols: int, n_mines: int) -> None:
        if rows <= 0 or cols <= 0:
            raise ValueError("Invalid rows or cols")

        if not (0 < n_mines < rows * cols):
            raise ValueError("Invalid number of mines")

        self.rows = rows
        self.cols = cols
        self.n_mines = n_mines

        self.board: list[list[int]] = [[0] * cols for _ in range(rows)]

        self.revealed: list[list[bool]] = [[False] * cols for _ in range(rows)]

        # Init the table
        self._place_mines()
        self._calculate_numbers()

    def _in_bounds(self, row: int, col: int) -> bool:
        return 0 <= row < self.rows and 0 <= col < self.cols

    def _neighbours(self, row: int, col: int) -> Generator[tuple[int, int], None, None]:
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue

                new_row = row + dr
                new_col = col + dc

                if self._in_bounds(new_row, new_col):
                    yield new_row, new_col

    def _place_mines(self) -> None:
        positions = list(range(self.rows * self.cols))
        random.shuffle(positions)

        for position in positions[: self.n_mines]:
            row = position // self.cols
            col = position % self.cols
            self.board[row][col] = Minesweeper.MINE

    def _calculate_numbers(self) -> None:
        # Calculates the mines for each slot
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == Minesweeper.MINE:
                    continue

                mine_count = 0
                for neighbour_row, neighbour_col in self._neighbours(row, col):
                    if self.board[neighbour_row][neighbour_col] == Minesweeper.MINE:
                        mine_count += 1
                self.board[row][col] = mine_count

    def reveal(self, row: int, col: int) -> bool:
        """
        Returns False if a mine is revealed. Otherwise, True.
        """
        if not self._in_bounds(row, col):
            raise IndexError("Invalid row or col")

        if self.board[row][col] == self.MINE:
            self.revealed[row][col] = True
            return False

        queue = deque([(row, col)])

        while queue:
            current_row, current_col = queue.popleft()

            if self.reavealed[current_row][current_col]:
                continue

            self.revealed[current_row][current_col] = True

            # Stop expanding once we reach a numbered square.
            if self.board[current_row][current_col] != 0:
                continue

            for neighbour_row, neighbour_col in self._neighbours(
                current_row, current_col
            ):
                if not self.revealed[neighbour_row][neighbour_col]:
                    queue.append((neighbour_row, neighbour_col))

        return True

    def at(self, row: int, col: int) -> int | None:
        if not self._in_bounds(row, col):
            raise IndexError("Row or col out of bounds")

        if not self.revealed[row][col]:
            return None

        return self.board[row][col]


if __name__ == "__main__":
    minesweeper = Minesweeper(10, 10, 10)
    pprint(minesweeper.board)
