class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open, close, s):
            if open == close == n:
                res.append(s)

            if open < n:
                backtrack(open+1, close, s + '(')
            
            if close < open:
                backtrack(open , close + 1, s + ')')

        backtrack(0,0,'')
        return res
            

        
