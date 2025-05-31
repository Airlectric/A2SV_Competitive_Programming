class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        if n == 0:
            return [-1,-1]

        left = 0
        right = n-1
        start = -1
        end = -1
        #  Bisect left
        while left < right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid+1
            else:
                right = mid

        if nums[left] != target:
            return [-1,-1]
        
        start = left

        # Bisect right
        left = start
        right = n-1

        while left < right:
            mid = (left + right+1) // 2

            if nums[mid] > target:
                right = mid-1
            else:
                left = mid

        end = left
        
        return [start,end]
        


        