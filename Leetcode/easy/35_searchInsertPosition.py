class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        pt1 = 0
        pt2 = len(nums)-1

        while pt1 <= pt2:

            pivot = abs(pt1 + pt2) // 2

            if nums[pivot] == target:
                return pivot
            
            if nums[pivot] < target:
                pt1 = pivot + 1
            elif nums[pivot] > target:
                pt2 = pivot - 1

        return pt1

        
        
        
        


        
