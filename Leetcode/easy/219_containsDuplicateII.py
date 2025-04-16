class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map_index = {}

        for i in range(len(nums)):
            if nums[i] not in map_index:
                map_index[nums[i]] = i
            elif nums[i] in map_index:
                if i - map_index[nums[i]] <= k:
                    return True
                map_index[nums[i]] = i
                
        return False
                

                
        
