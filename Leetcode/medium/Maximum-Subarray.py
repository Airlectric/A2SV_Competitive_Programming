class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = currentSum = nums[0]
        

        for num in nums[1:]:
            currentSum = max(num, currentSum+num)
            max_ = max(max_, currentSum)

        return max_
        