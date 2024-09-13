class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pt1 = 0
        pt2 = len(nums)-1

        while pt1 <= pt2:
            mid = (pt1 + pt2) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                pt2 = mid-1
            elif nums[mid] < target:
                pt1 = mid+1
        return -1


        
        
