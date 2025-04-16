class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        m = len(mat)
        n = len(mat[0])

        if m == 1:
            return mat[0]

        up = True
        row = 0
        col = 0
        result = []

        while len(result) < m * n:
            if up:
                result.append(mat[row][col])
                row -= 1
                col += 1
                
                if row < 0 and col >= n:
                    up = False
                    row += 2
                    col -= 1
                elif row < 0:
                    up = False
                    row += 1
                elif col >= n:
                    col -= 1
                    row += 2
                    up = False

            elif not up:
                result.append(mat[row][col])
                row += 1
                col -= 1
                if row >= m and col <= 0:
                    up = True
                    row -= 1
                    col += 2
                elif col < 0:
                    up = True
                    col += 1
                elif row >= m:
                    up = True
                    row -= 1
                    col += 2

        return result
            

                
            




        