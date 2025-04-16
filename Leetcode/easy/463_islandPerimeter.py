class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        peri = 0

        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    peri += 4

                    if i > 0 and grid[i-1][j] == 1:
                        peri -= 1
                    if i < row - 1 and grid[i+1][j] == 1:
                        peri -= 1
                    if j > 0 and grid[i][j-1] == 1:
                        peri -= 1
                    if j < column - 1 and grid[i][j+1]:
                        peri -= 1

        return peri
        
