class Solution:
    def longestPalindrome(self, s: str) -> str:
        substr = ''
        lenSub = 0

        for i in range(len(s)):
            pt1, pt2 = i, i
            while pt1 >= 0 and pt2 < len(s) and s[pt1] == s[pt2]:
                if (pt2 - pt1 + 1) > lenSub:
                    substr = s[pt1 : pt2+1]
                    lenSub = (pt2 - pt1 + 1)
                pt1-=1
                pt2+=1

            pt1, pt2 = i, i+1
            while pt1 >= 0 and pt2 < len(s) and s[pt1] == s[pt2]:
                if (pt2 - pt1 + 1) > lenSub:
                    substr = s[pt1 : pt2+1]
                    lenSub = (pt2 - pt1 + 1)
                pt1 -= 1
                pt2 += 1

        return substr



            

        
