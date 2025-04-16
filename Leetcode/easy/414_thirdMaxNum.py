class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinctNums = set(nums)
        revNums = sorted(distinctNums, reverse=True)

        if len(revNums) >= 3:
            return revNums[2]
        else:
            return revNums[0]
        
