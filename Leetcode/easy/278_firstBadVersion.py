# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        pt1 = 1
        pt2 = n


        while pt1 < pt2:
            pivot = (pt1 + pt2) >> 1

            if isBadVersion(pivot):
                pt2 = pivot
            else:
                pt1 = pivot + 1

        return pt2
        
