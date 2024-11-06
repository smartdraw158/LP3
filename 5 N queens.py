class NQueens:
    def __init__(self) -> None:
        self.size = int(input("Enter size of chessboard: "))
        self.board = [[False] * self.size for _ in range(self.size)]
        self.count = 0

    def printBoard(self):
        for row in self.board:
            for ele in row:
                if ele:
                    print("Q", end=" ")
                else:
                    print("X", end=" ")
            print()
        print()

    def isSafe(self, row: int, col: int) -> bool:
        # Check column for any queens
        for i in range(row):
            if self.board[i][col]:
                return False

        # Check backward slash (\) diagonal (above)
        i, j = row, col
        while i >= 0 and j >= 0:
            if self.board[i][j]:
                return False
            i -= 1
            j -= 1

        # Check forward slash (/) diagonal (above)
        i, j = row, col
        while i >= 0 and j < self.size:
            if self.board[i][j]:
                return False
            i -= 1
            j += 1

        return True

    def set_position_first_queen(self):
        print("Enter coordinates of the first queen:")
        row = int(input(f"Enter row (1-{self.size}): ")) - 1
        col = int(input(f"Enter column (1-{self.size}): ")) - 1
        self.board[row][col] = True
        self.printBoard()

    def solve(self, row: int):
        if row == self.size:
            self.count += 1
            self.printBoard()
            return

        # If there's a queen already in this row, skip to the next row
        if any(self.board[row]):
            self.solve(row + 1)
            return

        for col in range(self.size):
            if self.isSafe(row, col):
                self.board[row][col] = True
                self.solve(row + 1)
                self.board[row][col] = False

    def displayMessage(self):
        if self.count > 0:
            print("Solution exists for the given position of the queen.")
        else:
            print("Solution doesn't exist for the given position of the queen.")

# Main execution
solver = NQueens()
solver.set_position_first_queen()
solver.solve(0)
solver.displayMessage()
