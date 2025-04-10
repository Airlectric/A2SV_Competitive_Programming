class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if (m*n) != (r*c):
            return mat
        
        if m == r and n == c:
            return mat

        new_mat = [[0 for _ in range(c)] for _ in range(r)]

        temp = []

        for i in range(m):
            for j in range(n):
                temp.append(mat[i][j])

        count = 0

        for i in range(r):
            for j in range(c):
                new_mat[i][j] = temp[count]
                count += 1
        
        return new_mat
        