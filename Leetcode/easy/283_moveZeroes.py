class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        
        nonzero = 0

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[nonzero] = nums[j]
                nonzero += 1

        while nonzero < len(nums):
            nums[nonzero] = 0
            nonzero += 1

        return nums        
