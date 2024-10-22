class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        j = 0
        new = ''

        for i in range(len(t)):
            if j < len(s) and s[j] == t[i]:
                new += t[i]
                j+=1

        return new == s

        
