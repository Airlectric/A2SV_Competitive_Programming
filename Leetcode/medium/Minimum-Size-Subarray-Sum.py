class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        min_len = float('inf')
        n = len(nums)
        window_sum = 0

        for end in range(n):
            window_sum += nums[end]
            while window_sum >= target:
                print(window_sum)
                min_len = min(min_len, end-start+1)
                window_sum -= nums[start]
                start += 1
                    
        return min_len if min_len != float('inf') else 0





        