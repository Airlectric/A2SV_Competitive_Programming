from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        charCount = Counter(s)
        longest = 0
        foundOdd = False

        for count in charCount.values():
            if count % 2 == 0:
                longest += count
            else:
                foundOdd = True
                longest += count - 1
        
        if foundOdd:
            longest += 1

        return longest
        
