class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        \\\
        Do not return anything, modify nums in-place instead.
        \\\
        pt1, pt2 = 0,0

        while pt2 < len(nums):
            if nums[pt2] != 0:
                nums[pt1], nums[pt2] = nums[pt2], nums[pt1]
                pt1 += 1
                pt2 += 1
            else:
                pt2 += 1
