class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = s.replace('-','')
        result = ''
        count = 0
        mul = 0

        res = res[::-1]

        while count < len(res):
                if count > 0:
                    result += '-'
                result += res[mul:mul + k]
                count += k
                mul += k

        return result[::-1].upper()


        
