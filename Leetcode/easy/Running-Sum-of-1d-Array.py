class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefixSum = [0] * (n+1)

        for i in range(n):
            prefixSum[i+1] = prefixSum[i] + nums[i]

        return prefixSum[1:]
        