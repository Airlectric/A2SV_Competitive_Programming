class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        pos_sum = 0
        arr_sum = 0

        for i in range(len(nums)):
            pos_sum += i + 1
            arr_sum += nums[i]

        return pos_sum - arr_sum
        
