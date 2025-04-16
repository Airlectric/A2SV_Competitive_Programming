class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        g.sort()
        s.sort()
        i = len(g)-1
        j = len(s)-1

        while j >= 0 and i >= 0:
            if s[j] >= g[i]:
                res += 1
                i -= 1
                j -= 1
            else:
                i -= 1
        return res
        
