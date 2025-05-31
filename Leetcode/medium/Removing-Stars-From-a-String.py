class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for ele in s:
            if stack and ele == '*':
                stack.pop()
            else:
                stack.append(ele)
        
        return ''.join(stack)

        