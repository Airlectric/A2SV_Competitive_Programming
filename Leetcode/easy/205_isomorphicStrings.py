from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        if len(s) == len(t) == 1:
            return True
        
        detect = defaultdict(list)

        for i in range(len(s)):
            if s[i] not in detect:
                if t[i] in detect.values():
                    return False
                detect[s[i]] = t[i]
            elif s[i] in detect:
                if detect[s[i]] != t[i]:
                    return False
        return True

        
