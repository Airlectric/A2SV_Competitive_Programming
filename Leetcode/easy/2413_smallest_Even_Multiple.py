class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n % 2 == 0:
            return n
        
        counter = 0
        found = True
        value = 0
        while found:
            counter+=1
            if (counter * n) % 2 == 0:
                value = counter * n
                found = False
        return value

        
