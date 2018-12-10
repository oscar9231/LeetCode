class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        row_zero_index = []
        col_zero_index = []
        for row in range(0, m):
            for col in range(0, n):
                if matrix[row][col] == 0:
                    row_zero_index.append(row)
                    col_zero_index.append(col)
        for i in row_zero_index:
            matrix[i] = [0] * n
        for j in col_zero_index:
            for i in range(m):
                matrix[i][j] = 0
