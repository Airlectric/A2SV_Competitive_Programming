class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []

        for ele in s:
            if s_stack and ele == '#':
                s_stack.pop()
            else:
                if ele != '#':
                    s_stack.append(ele)
        
        for ele in t:
            if t_stack and ele == '#':
                t_stack.pop()
            else:
                if ele != '#':
                    t_stack.append(ele)
        return s_stack == t_stack

        