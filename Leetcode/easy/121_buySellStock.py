class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pt1 = 0
        pt2 = 1

        maxprofit = 0

        while pt2 < len(prices):
            if prices[pt2] > prices[pt1]:
                profit = prices[pt2] - prices[pt1]
                maxprofit = max(profit, maxprofit)
            else:
                pt1=pt2
            pt2 += 1
        return maxprofit
        
