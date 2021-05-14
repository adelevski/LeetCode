
class NumMatrix:

    def __init__(self, matrix):
        M,N = len(matrix), len(matrix[0])
        
        self.dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
        for r in range(1, M+1):
            for c in range(1, N+1):
                self.dp[r][c] = matrix[r-1][c-1] + self.dp[r][c-1]
        

    def sumRegion(self, row1, col1, row2, col2):
        output = 0
        for r in range(row1+1, row2+2):
            output += self.dp[r][col2+1]-self.dp[r][col1]
        return output
                
                
matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]

# row1, col1, row2, col2 = 2, 1, 4, 3 # Output = 8
# row1, col1, row2, col2 = 1, 1, 2, 2 # Output = 11
# row1, col1, row2, col2 = 1, 2, 2, 4 # Output = 12


obj = NumMatrix(matrix)
param_1 = obj.sumRegion(row1, col1, row2, col2)
print(param_1)