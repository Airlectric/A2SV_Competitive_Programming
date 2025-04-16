class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        numerals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i = 0

        while i < len(s):
            if i+1 < len(s) and numerals[s[i+1]] > numerals[s[i]]:
                num += numerals[s[i+1]] - numerals[s[i]]
                i+=1
            else:
                num+= numerals[s[i]]
            i+=1
        
        return num

        
