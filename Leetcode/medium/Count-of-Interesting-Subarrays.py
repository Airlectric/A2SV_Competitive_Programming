from collections import defaultdict

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)

        indicator = [0] * n

        for i in range(n):
            if nums[i] % modulo == k:
                indicator[i] = 1

        seenBefore = defaultdict(int)
        seenBefore[0] = 1
        count = 0
        prefixSumR = 0

        for i in range(n):
            prefixSumR += indicator[i]
            modVal = (prefixSumR % modulo)
            target = (modVal - k) % modulo # to handle negative values

            if target in seenBefore:
                count += seenBefore[target]
                seenBefore[modVal] += 1
            else:
                seenBefore[modVal] += 1
        
        return count
        




        