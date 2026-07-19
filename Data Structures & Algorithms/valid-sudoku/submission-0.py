class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            d = {}
            for col in range(len(board)):
                num = board[row][col]
                if num == ".": continue
                if num in d:
                    return False
                d[num] = num

        for col in range(len(board)):
            d = {}
            for row in range(len(board)):
                num = board[row][col]
                if num == ".": continue
                if num in d:
                    return False
                d[num] = num

        d = {}
        for row in range(len(board)):
            for col in range(len(board)):
                num = board[row][col]
                key = (row//3,col//3)
                if num == ".": continue
                if key in d:
                    if num in d[key]:
                        return False
                    d[key].append(num) 
                else:
                    d[key] = [num]
        return True
