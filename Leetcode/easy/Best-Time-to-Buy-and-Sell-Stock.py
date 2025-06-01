class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        max_profit = 0

        n = len(prices)

        for end in range(n):

            if prices[end] < buy:
                buy = prices[end]
            else:
                max_profit = max(max_profit, prices[end] - buy)

        return max_profit



            
        