class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) > len(haystack):
            return -1

        k = len(needle)
        first = needle[0]
        count = 1

        for end in range(len(haystack)):
            if first == haystack[end]:
                if needle == haystack[end:end+k]:
                    return end
        return -1
                        

        
