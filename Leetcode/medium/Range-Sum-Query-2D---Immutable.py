class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        m = len(self.matrix)
        n = len(self.matrix[0])

        self.prefixMatrix = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                self.prefixMatrix[i+1][j+1] = self.matrix[i][j] + self.prefixMatrix[i+1][j] \\
                + self.prefixMatrix[i][j+1] - self.prefixMatrix[i][j]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        sum_ = self.prefixMatrix[row2+1][col2+1] - self.prefixMatrix[row2+1][col1] - \\
        self.prefixMatrix[row1][col2+1] + self.prefixMatrix[row1][col1]

        return sum_


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)