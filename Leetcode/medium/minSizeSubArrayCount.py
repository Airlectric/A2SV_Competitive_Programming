class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        minlen = 0
        start = 0
        summation = 0

        for end in range(len(nums)):
            summation+=nums[end]
            while summation >= target:
                if minlen == 0:
                    minlen = end - start + 1
                minlen = min(minlen, (end-start+1))
                summation-=nums[start]
                start+=1
        return minlen

        
