from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        seenBefore = defaultdict(int)
        count = 0
        prefixSum = 0
        seenBefore[0] = 1
        n = len(nums)

        for i in range(n):
            if (nums[i] % 2) == 1:
                nums[i] = 1 
            else:
                nums[i] = 0

        for i in range(n):
            prefixSum += nums[i]
            diff = prefixSum - k

            if diff in seenBefore:
                count += seenBefore[diff]
                seenBefore[prefixSum] += 1
            else:
                seenBefore[prefixSum] += 1
        
        return count





        