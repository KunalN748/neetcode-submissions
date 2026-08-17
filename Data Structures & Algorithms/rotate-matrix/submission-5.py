class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for row in range(len(matrix)-1):
            for col in range(row, len(matrix[row])):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        for row in matrix:
            row.reverse()
        


