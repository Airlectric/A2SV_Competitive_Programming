from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)
        count_t = Counter(t)

        for i in range(len(t)):
            if count_s[t[i]] != count_t[t[i]]:
                return t[i]

        
