class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
    
        big = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            pt1, pt2 = i+1, len(nums)-1
            small = []
            while pt1 < pt2:
                result = nums[pt1] + nums[i] + nums[pt2]
                if result == 0:
                    small = [nums[pt1], nums[i], nums[pt2]]
                    big.append(small)
                    pt1 += 1
                    pt2 -= 1
                    while nums[pt1] == nums[pt1-1] and pt1 < pt2:
                        pt1 +=1
                    while pt1 < pt2 and nums[pt2] == nums[pt2+1]:
                        pt2 -= 1
                elif result > 0:
                    pt2 -= 1
                else:
                    pt1 += 1
        return big



        
