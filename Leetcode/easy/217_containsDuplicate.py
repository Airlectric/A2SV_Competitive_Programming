class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        detect = set()

        for num in nums:
            if num not in detect:
                detect.add(num)
            elif num in detect:
                return True

        return False
        
