class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]

            if complement in num_idx:
                return [i,num_idx[complement]]
            else:
                num_idx[nums[i]] = i
            




        