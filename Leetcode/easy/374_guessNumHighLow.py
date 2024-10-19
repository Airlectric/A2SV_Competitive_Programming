# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return n

        pt1 = 1
        pt2 = n

        while pt1 <= pt2:
            num = (pt1 + pt2) >> 1

            if guess(num) == -1:
                pt2 = num - 1
            elif guess(num) == 1:
                pt1 = num + 1
            elif guess(num) == 0:
                return num

        
