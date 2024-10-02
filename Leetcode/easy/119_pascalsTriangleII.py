class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        dp = [None] * (rowIndex+1)
        print(dp)
        dp[0] = [1]
        dp[1] = [1,1]

        if rowIndex == 1:
            return dp[rowIndex]

        for i in range(2,rowIndex+1):
            s = 0
            dp[i] = []
            while s != i-1:
                value = dp[i-1][s] + dp[i-1][s+1]
                dp[i].append(value)
                s+=1
            dp[i] = [1] + dp[i] + [1]
        return dp[rowIndex]

    
        
