from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        start = 0
        max_ = float('-inf')
        detect = defaultdict(int)
        diff = 0

        for end in range(n):
            detect[s[end]] += 1
            diff = (end-start+1) - max(detect.values())

            if diff > k:
                while diff > k:
                    detect[s[start]] -= 1
                    start += 1
                    diff = (end-start+1) - max(detect.values())
    
            max_ = max(max_, end-start+1)
         
        return max_





            
            



        