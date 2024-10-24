class Solution:
    def toHex(self, num: int) -> str:
        letters = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
        res = ''
        count = 0
        if not num:
            return "0"

        if num < 0:
            num = ~(-1 * num) + 1

        while num != 0 and count < 8:
            remainder = num % 16
            if remainder > 9 and remainder < 16:
                res += letters[remainder]
            else:
                res += str(remainder)
            num //= 16
            count += 1

        return res[::-1]


        
        
