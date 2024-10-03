class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None:
            return True
        s = s.lower()
        s = s.split(' ')
        s = ''.join(s)

        new_s = ''
        for char in s:
            if char.isalnum():
                new_s+=char

        revS = new_s[::-1]
        return new_s == revS


        
