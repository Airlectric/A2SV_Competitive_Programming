class Solution:
    def findComplement(self, num: int) -> int:
        res = ""
        result = 0

        while num != 1:
            remainder = num % 2
            if remainder == 1:
                res += '0'
            else:
                res += '1'
            num //= 2

        res += "0"

        for i in range(len(res)):
            result += int(res[i]) * 2 ** i

        return result


        
        
        
