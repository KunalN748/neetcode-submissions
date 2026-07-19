class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [set() for _ in range(len(board))]
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board))]

        for row in range(len(board)):
            for col in range(len(board)):
                num = board[row][col]
                if num == ".": continue
                box = (row//3) * 3 + col//3
                if num in rows[row] or num in cols[col] or num in boxes[box]:
                    return False
                cols[col].add(num)
                rows[row].add(num)
                boxes[box].add(num)
        return True
