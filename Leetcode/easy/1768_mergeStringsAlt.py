class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        determinant = min(len(word1), len(word2))
        print(determinant)
        count = 0
        new=""
        for i in range(determinant):
            new+=word1[i]
            new+=word2[i]

        if len(word1) < len(word2) and len(word1) != len(word2) :
            new+=word2[determinant:]
        else:
            new+=word1[determinant:]
        return new


    


        
