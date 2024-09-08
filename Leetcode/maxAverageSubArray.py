class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        maximum = float('-inf')
        summation = 0
        start = 0

        for end in range(len(nums)):
            summation += nums[end]
            if (end-start+1) == k:
                aveg = float(summation)/float(k)
                if aveg > maximum:
                    maximum = aveg
                summation-=nums[start]
                start+=1
        return maximum

        
