class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        invert_s = s[::-1]

        i = 0

        for j in range(len(s)):
            if invert_s[j] != " ":
                i+=1
            elif i != 0 and invert_s[j]==" ":
                return i
        return i
        
