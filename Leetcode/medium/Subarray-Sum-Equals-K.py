from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        count = 0
        prefixSumCount = defaultdict(int)
        prefixSumCount[0] = 1

        for i in range(len(nums)):
            prefixSum += nums[i]

            if (prefixSum-k) in prefixSumCount:
                count += prefixSumCount[prefixSum-k]
                prefixSumCount[prefixSum] += 1
            else:
                prefixSumCount[prefixSum] += 1
        
        return count
        