class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        pt1 = 0
        pt2 = n-1

        while pt1 < pt2:
            result = numbers[pt1] + numbers[pt2]

            if result == target:
                return [pt1+1, pt2+1]
            if result < target:
                pt1 += 1
            else:
                pt2 -= 1

        