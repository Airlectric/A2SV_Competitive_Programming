class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        s = s.strip()

        if len(s) == 0:
            return 0
            
        stop = 0
        sign = 1
        
        if s[0] == '-' or s[0] == '+':
            if s[0] == "-":
                sign = -1
            s = s[1:]

        while stop < len(s) and s[stop].isdigit():
            stop += 1
        
        if stop:
            s = s[:stop]
            s = int(s) * sign
        else:
            return 0

        if s > INT_MAX:
            return INT_MAX
        elif s < INT_MIN:
            return INT_MIN
        else:
            return s
        
        


        
