from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longstr = 0
        start = 0
        detect = defaultdict(bool)

        for end in range(len(s)):
            if not detect[s[end]]:
                detect[s[end]] = True
                longstr = max(longstr, (end-start+1))
            else:
                while detect[s[end]]:
                    detect[s[start]] = False
                    start +=1
                detect[s[end]]=True
        return longstr



    
        
