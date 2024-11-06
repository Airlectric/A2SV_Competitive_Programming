class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = ''
        result = ''
        count = 0
        mul = 0

        for i in range(len(s)):
            if s[i].isalnum():
                if s[i].isalpha():
                    res += s[i].upper()
                else:
                    res += s[i]
        res = res[::-1]

        while count < len(res):
                if count > 0:
                    result += '-'
                result += res[mul:mul + k]
                count += k
                mul += k

        return result[::-1]


        
