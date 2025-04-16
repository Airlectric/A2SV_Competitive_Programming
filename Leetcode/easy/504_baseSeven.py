class Solution:
    def convertToBase7(self, num: int) -> str:
        neg = 0
        if num < 0:
            num = abs(num)
            neg += 1
        elif num == 0:
            return '0'

        res = ''
        while num != 0:
            remainder = num % 7
            res += str(remainder)
            num //= 7
        
        if neg == 1:
            res += '-'
        return res[::-1]


        
