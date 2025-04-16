class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        paren = {')':'(','}':'{',']':'['}
        stack = []

        for bracket in s:
            if bracket in paren:
                if not stack:
                    return False
                top = stack.pop()
                if paren[bracket] != top:
                    return False
            else:
                stack.append(bracket)
                
        if not stack:
            return True
        else:
            return False

        
