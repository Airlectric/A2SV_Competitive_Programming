class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = len(s)

        for char in s:

            if char == ']':

                substr = []
                while stack[-1] != '[':
                    substr.append(stack.pop())
                stack.pop()

                num = []
                while stack and stack[-1].isnumeric():
                    num.append(stack.pop())
                
                multiplier = int(''.join(num[::-1]))
                
                decoded = ''.join(substr[::-1]) * multiplier
                stack.append(decoded)
            else:
                stack.append(char)

        return ''.join(stack)



        


        