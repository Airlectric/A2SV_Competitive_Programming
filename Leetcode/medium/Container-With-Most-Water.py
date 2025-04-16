class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_ = float('-inf')

        N = len(height)

        i = 0
        j = N - 1
        area = 0

        while i < j:
            length = min(height[i], height[j])
            width = j - i
            area = length * width
            max_ = max(area, max_)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return max_


        