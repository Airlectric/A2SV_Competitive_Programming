class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        right_ones = sum(nums)
        left_zeros = 0
        n = len(nums)
        track_score = []

        for i in range(n+1):
            score = right_ones + left_zeros
            track_score.append(score)

            if i < n:
                if nums[i] == 0:
                    left_zeros += 1
                else:
                    right_ones -= 1

        max_score = max(track_score)

        result = [i for i,v in enumerate(track_score) if v == max_score]

        return result

        