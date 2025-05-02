from collections import defaultdict

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        result = [-1] * n
        stack = []
        track = defaultdict(int)

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                track[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        
        for i in range(len(nums1)):
            result[i] = track[nums1[i]] if track[nums1[i]] != 0 else -1
        
        return result
        

            

       

        