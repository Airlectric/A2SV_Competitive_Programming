class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        seenBefore = {0:-1}
        small = float('inf')
        prefixSumR = 0
        total = sum(nums)

        if total % p == 0:
            return 0

        for i in range(n):
            prefixSumR += nums[i]
            target =  ((prefixSumR % p) - (total % p)) % p
            if target in seenBefore:
                small = min(small, (i-seenBefore[target]))
                seenBefore[prefixSumR % p] = i
            else:
                seenBefore[prefixSumR % p] = i
        
        return small if small < n else -1

        