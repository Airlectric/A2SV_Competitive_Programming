class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        left = 1
        right = x
        sqroot = 0

        while left <= right:
            pivot = (left + right) // 2
            check = pivot * pivot

            if check == x:
                return pivot

            elif check < x:
                sqroot = pivot
                left = pivot + 1
            else: 
                right = pivot -1
        return sqroot
        
