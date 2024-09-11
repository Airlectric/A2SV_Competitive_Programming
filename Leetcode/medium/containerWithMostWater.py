class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        pt1 = 0
        pt2 = len(height)-1
        area = 0

        while pt1 < pt2:
            breath = pt2-pt1
            length = min(height[pt1],height[pt2])
            area = max(area, (length * breath))

            if height[pt1] < height[pt2]:
                pt1+=1
            else:
                pt2-=1

        return area


        
