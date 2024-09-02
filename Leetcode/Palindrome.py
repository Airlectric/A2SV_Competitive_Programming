class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        st_x = str(x)
        rev_x = st_x[::-1]
        if st_x == rev_x:
            return True
        else:
            return False
        