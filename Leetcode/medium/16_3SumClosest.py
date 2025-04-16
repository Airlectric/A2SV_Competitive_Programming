class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        diff = float('inf')

        for i in range(len(nums)):
            pt1, pt2 = i+1, len(nums)-1
            while pt1 < pt2:
                sumup = nums[i] + nums[pt1] + nums[pt2]
                if sumup == target:
                    res = sumup
                    return res
                elif abs(sumup - target) < diff:
                        diff = abs(sumup - target)
                        res = sumup
                elif sumup > target:
                    pt2 -= 1
                else:
                    pt1 += 1
        return res
                
                    

        
