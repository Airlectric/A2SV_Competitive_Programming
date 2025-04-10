class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        \\\
        Do not return anything, modify matrix in-place instead.
        \\\
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    a = 0 
                    b = 0
                    check = True
                    while check:
                        if a < m and matrix[a][j] != 0:
                            matrix[a][j] = 'i'
                        if b < n and matrix[i][b] != 0:
                            matrix[i][b] = 'i'

                        a += 1
                        b += 1

                        if a > m-1 and b > n-1:
                            check = False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'i':
                    matrix[i][j] = 0


        