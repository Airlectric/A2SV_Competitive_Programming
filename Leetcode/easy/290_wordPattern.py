class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        detect = {}
        s = s.split()
        if len(s) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in detect:
                if s[i] in detect.values():
                    return False
                detect[pattern[i]] = s[i]
            elif detect[pattern[i]] != s[i]:
                return False
        return True

        
