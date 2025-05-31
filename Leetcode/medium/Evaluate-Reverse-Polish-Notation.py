class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'*','/','+','-'}

        for i in range(len(tokens)):
            if stack and tokens[i] in operators:
                a = stack.pop()
                b = stack.pop()
                if tokens[i] == '*':
                    res = b * a
                elif tokens[i] == '+':
                    res = b + a
                elif tokens[i] == '-':
                    res = b - a
                else:
                    res = int(b / a)
                stack.append(res)
            else:
                stack.append(int(tokens[i]))

        return stack[0]