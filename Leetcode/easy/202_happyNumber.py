class Solution:
    def isHappy(self, n: int) -> bool:
        Loop = []

        while n != 1:
            if n in Loop:
                return False
            Loop.append(n)
            num = 0
            while n != 0:
                digit = n % 10
                num += digit ** 2
                n //= 10
            n = num

        return True

        
