class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        pt1 = 0
        pt2 = len(numbers)-1
        summation = 0

        while pt1 < pt2:
            summation = numbers[pt1] + numbers[pt2]

            if summation == target:
                return [pt1+1,pt2+1]
            elif summation > target:
                pt2 -= 1
            else:
                pt1 += 1
        
