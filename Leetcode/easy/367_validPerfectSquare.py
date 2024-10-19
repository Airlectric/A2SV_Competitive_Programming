class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        res = num ** 0.5 

        if res % 1 == 0:
            return True
        else:
            return False
