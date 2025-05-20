from math import ceil

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        def estimatedDays(capacity):
            num_of_days = 1
            prev_weight = 0

            for weight in weights:
                if prev_weight + weight > capacity:
                    num_of_days += 1
                    prev_weight = 0
                prev_weight += weight
            return num_of_days

        while left < right:
            mid = left + (right - left) // 2

            if estimatedDays(mid) <= days:
                right = mid
            else:
                left = mid + 1
        
        return left
        