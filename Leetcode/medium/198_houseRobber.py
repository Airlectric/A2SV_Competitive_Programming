class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]

        maxmoney = [None] * len(nums)
        maxmoney[0] = nums[0]
        maxmoney[1] = max(nums[0],nums[1])

        for i in range(2, len(nums)):
            maxmoney[i] = max(nums[i]+maxmoney[i-2], maxmoney[i-1])

        return maxmoney[-1]
        
