class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        result = []

        count_ = [0] * (max(nums)+1)

        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums)):
                count_[sorted_nums[i]] = sorted_nums.index(sorted_nums[i])

        for num in nums:
            result.append(count_[num])

        return result


        