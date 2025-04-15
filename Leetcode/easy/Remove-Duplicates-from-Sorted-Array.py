class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        i = 0
        j = 1

        k = 1
        while j < N:
            if nums[i] == nums[j]:
                j += 1
            elif nums[i] != nums[j]:
                k += 1
                nums[i+1] = nums[j]
                i += 1
                j += 1

        return k
            

        