class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'}':'{',')':'(',']':'['}
        stack = []
        
        for bracket in s:
            if bracket in brackets:
                close = stack.pop() if stack else ''
                
                if brackets[bracket] != close:
                    return False
            else:
                stack.append(bracket)

        return len(stack) == 0
