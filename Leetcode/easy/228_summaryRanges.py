class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
        length = len(nums)
        i = 0
        res = []

        while i < length:
            j = nums[i]
            count = i
            while j in nums:
                count += 1
                j +=1

            if nums[i] == nums[count-1]:
                res.append(f"{nums[i]}")
            else:
                res.append(f"{nums[i]}->{nums[count-1]}")

            i = count

        return res

        
