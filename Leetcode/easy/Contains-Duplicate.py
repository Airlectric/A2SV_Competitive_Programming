class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        detect = set()

        for num in nums:
            if num in detect:
                return True
            detect.add(num)
        
        return False
        