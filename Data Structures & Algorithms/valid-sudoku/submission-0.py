class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            numbers = set()
            for j in range(9):
                if not addNumber(numbers, board[i][j]):
                    return False
        for j in range(9):
            numbers = set()
            for i in range(9):
                if not addNumber(numbers, board[i][j]):
                    return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                numbers = set()
                for di in range(3):
                    for dj in range(3):
                        if not addNumber(numbers, board[i + di][j + dj]):
                            return False
        return True

def addNumber(numbers, n):
    if n == ".":
        return True
    if n in numbers:
        return False
    else:
        numbers.add(n)
        return True