from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == \\:
            return 0
            
        detect = defaultdict(int)
        N = len(s)
        start = 0
        str_len = float('-inf')

        for end in range(N):
            detect[s[end]] += 1

            while detect[s[end]] > 1:
                detect[s[start]] -= 1
                start += 1
            
            str_len = max(str_len, end-start+1)
        
        return str_len
            



        