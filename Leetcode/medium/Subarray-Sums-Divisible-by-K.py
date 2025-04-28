from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSum = 0
        count = 0
        seenBefore = defaultdict(int)
        seenBefore[0] = 1

        for i in range(n):
            prefixSum += nums[i]
            mod = (prefixSum % k)
            if mod < 0:
                mode += k
            if mod in seenBefore:
                count += seenBefore[mod]
                seenBefore[mod] += 1
            else:
                seenBefore[mod] += 1
        
        return count

            

        