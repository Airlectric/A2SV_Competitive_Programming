class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                pt1, pt2 = j+1, n-1
                while pt1 < pt2:
                    sumup = nums[i] + nums[j] + nums[pt1] + nums[pt2]
                    if sumup == target:
                        res.append([nums[i],nums[j],nums[pt1],nums[pt2]])

                        pt1 += 1
                        pt2 -= 1
                        while pt1 < pt2 and nums[pt1] == nums[pt1-1]:
                            pt1 += 1
                        while pt1 < pt2 and nums[pt2] == nums[pt2+1]:
                            pt2 -= 1
                        
                    elif sumup > target:
                        pt2 -= 1
                    else:
                        pt1 += 1
        return res

        
