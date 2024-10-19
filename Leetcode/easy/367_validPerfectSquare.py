class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        res = num ** 0.5

        return res % 1 == 0

      
