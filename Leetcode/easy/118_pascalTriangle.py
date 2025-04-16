class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return
        if numRows == 1:
            return [[1]]

        dp = [None] * (numRows)
     
        dp[0] = [1]
        dp[1] = [1,1]

        for i in range(2, numRows):
            s = 0
            dp[i] = []
            while s != i-1:
                value = dp[i-1][s] + dp[i-1][s+1]
                dp[i].append(value)
                s+=1
            dp[i] = [1] + dp[i] + [1]

        return dp
        
        
