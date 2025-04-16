class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        count = 0
        total = len(s)

        for i in range(total):
            if s[i] == letter:
                count+=1
                
        percent = (float(count)/ float(total)) * 100
        return int(percent)

        
