class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isRightDiagonal(grid):
            calculate = 0
            track = []
            for i in range(3):
                if 0 < grid[i][i] <= 9:
                    calculate += grid[i][i]
            
            if calculate == 15:
                return True
            return False

        def isLeftDiagonal(grid):
            calculate = 0
            track = []
            for i in range(3):
                if 0 < grid[i][3-i-1] <= 9:
                    track.append(grid[i][3-i-1])

            if len(set(track)) == 3:
                calculate = sum(track)
            
            if calculate == 15:
                return True
            return False
        
        def isHorizontal(grid):
            for i in range(3):
                calculate = 0
                for j in range(3):
                    if 0 < grid[i][j] <= 9:
                        calculate += grid[i][j]
                if calculate != 15:
                    return False
            
            return True


        def isVertical(grid):
            for j in range(3):
                calculate = 0
                for i in range(3):
                    if 0 < grid[i][j] <= 9:
                        calculate += grid[i][j]
                if calculate != 15:
                    return False
            
            return True

        numOfSubgrids = 0

        if len(set(grid[0])) == 1:
            return 0

        down = 0
        while down+3 <= len(grid):
            for i in range(len(grid)):
                sub_grid = []
                for j in range(down,3+down):
                    if 0<= j <= len(grid) and 0<= i+3 <= len(grid[0]):
                        print(j)
                        sub_grid.append(grid[j][i:3+i])

                if len(sub_grid) > 0 and isRightDiagonal(sub_grid) and isLeftDiagonal(sub_grid) and isVertical(sub_grid) and isHorizontal(sub_grid):
                    numOfSubgrids += 1
            
            down += 1

        return numOfSubgrids



        
        

        