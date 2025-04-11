class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        result = []
        left_col , right_col = 0, n-1
        top_row, bottom_row = 0, m-1

        while top_row <= bottom_row and left_col <= right_col:
            # moving right
            for col in range(left_col, right_col+1):
                result.append(matrix[top_row][col])
            top_row += 1
            
            # moving down
            for row in range(top_row, bottom_row+1):
                result.append(matrix[row][right_col])
            right_col -= 1
            
            # moving left
            if top_row <= bottom_row:
                for col in range(right_col,left_col - 1 ,-1):
                    result.append(matrix[bottom_row][col])
            bottom_row -= 1

            # moving up
            if left_col <= right_col:
                for row in range(bottom_row,top_row - 1,-1):
                    result.append(matrix[row][left_col])
            left_col += 1

        return result



        


        