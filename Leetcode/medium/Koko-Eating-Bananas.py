from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right-left) // 2

            test_hours = sum(ceil(pile/mid) for pile in piles)

            if test_hours <= h:
                right = mid
            else:
                left = mid + 1

        return left 
        