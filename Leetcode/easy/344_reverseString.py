class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        pt1, pt2 = 0, len(s)-1

        while pt1 < pt2:
            holder = s[pt1]
            s[pt1] = s[pt2]
            s[pt2] = holder
            pt1 += 1
            pt2 -= 1
        
        return s

        
        
