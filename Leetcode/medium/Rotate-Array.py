class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        \\\
        Do not return anything, modify nums in-place instead.
        \\\
        if k == 0:
            return nums

        if k > len(nums):
            k = k % len(nums)
        

        nums[:] = nums[::-1]

        if k == 0:
            return nums
        else:
            nums[:] = nums[k-1::-1] + nums[k::][::-1]
        