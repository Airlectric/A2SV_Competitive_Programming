class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
       
        for digit in nums1:
            if digit in nums2 and digit not in res:
                res.append(digit)
                
        return res


        
