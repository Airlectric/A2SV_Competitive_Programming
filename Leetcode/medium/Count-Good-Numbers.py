from math import ceil

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even = ceil(n/2)
        odd = n // 2
        MOD = 10**9 + 7

        def powOfNum(num,exp):
            if exp == 0:
                return 1
            if num == 0:
                return 0

            half = powOfNum(num, exp // 2)
            result = (half * half) % MOD
            return (result * num) % MOD if exp % 2 else result
        
        return (powOfNum(5,even) * powOfNum(4,odd)) % MOD
        