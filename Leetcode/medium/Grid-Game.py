class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        result = float('-inf')
        m = len(grid[0])

        prefixSumr0 = [0] * (m+1)

        for i in range(m):
            prefixSumr0[i+1] = prefixSumr0[i] + grid[0][i]

        totalr0 = prefixSumr0[-1]
        suffixSumr1 = 0

        for i in range(m):
            totalr0 -= grid[0][i]
            suffixSumr1 += grid[1][i]
            result = max(result, min(totalr0,suffixSumr1))
        
        return result


            
        
    
        
        return 4


        
        