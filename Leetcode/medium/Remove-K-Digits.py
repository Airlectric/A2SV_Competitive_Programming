class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        n = len(num)
        print('n',n)

        for i in range(n):
            while stack and k > 0 and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])

        while stack and k > 0:
            stack.pop()
            k -= 1
        
        result = ''.join(stack).lstrip('0')

        return result if result else '0'
        