class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float(\-inf\)

        start = 0
        end = k-1
        max_ = sum(nums[:k])

        while end < len(nums):
            max_avg = max(max_avg, max_)

            max_ = max_ - nums[start]
            start += 1
            end += 1
            if end < len(nums):
                max_ = max_ + nums[end]
        
        return max_avg/k


            
        