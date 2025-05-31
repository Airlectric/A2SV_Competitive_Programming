from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        seenBefore = defaultdict(int)
        count = 0
        n = len(nums)
        seenBefore[0] = 1
        prefixSum = 0

        for i in range(n):
            prefixSum += nums[i]
            diff = prefixSum - goal
            if diff in seenBefore:
                count += seenBefore[diff]
                seenBefore[prefixSum] += 1
            else:
                seenBefore[prefixSum] += 1
        
        return count

        