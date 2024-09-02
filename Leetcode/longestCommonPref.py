class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefs=""
        word = strs[0]
        for item in strs[1:]:
            i = 0
            while i<len(word) and i<len(item) and word[i]==item[i]:
                i+=1
            prefs=word[:i]
            if prefs == "":
                return ""
        return prefs

        