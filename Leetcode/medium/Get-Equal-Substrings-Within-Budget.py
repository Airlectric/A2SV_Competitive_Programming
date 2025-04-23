class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)

        if s == t:
            return n
            
        max_ = float('-inf')
        start = 0
        cost = 0

        for end in range(n):
            cost += abs(ord(s[end])-ord(t[end]))
            if cost > maxCost:
                while cost > maxCost:
                    cost -= abs(ord(s[start])-ord(t[start]))
                    start += 1
            elif cost < maxCost:
                max_ = max(max_, end-start+1)
            else:
                max_ = max(max_, end-start+1)
                cost -= abs(ord(s[start])-ord(t[start]))
                start += 1

        return max_ if max_ != float('-inf') else 0



        