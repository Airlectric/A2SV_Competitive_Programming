class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pt1 = 0
        pt2 = len(nums)-1

        while pt1 < pt2:
            mid = (pt1 + pt2 ) // 2

            if nums[mid] < nums[mid+1]:
                pt1 = mid+1
            elif nums[mid] > nums[mid+1]:
                pt2 = mid

        return pt2
        
