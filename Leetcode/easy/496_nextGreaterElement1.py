class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        mapIndex = {}
        for i in range(len(nums2)):
            mapIndex[nums2[i]] = i

        for j in range(len(nums1)):
            index = mapIndex[nums1[j]]
            k = 0
            while k < len(nums2):
                if index + k < len(nums2) and nums2[index + k] > nums2[index]:
                    res.append(nums2[index + k])
                    k = len(nums2)
                elif index + k  == len(nums2)-1 and nums2[index + k] == nums2[-1]:
                    res.append(-1)
                k += 1

        return res

        
