from collections import defaultdict

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0] * n
        intervals = defaultdict(int)

        for i in range(n):
            while stack and stack[-1][0] < temperatures[i]:
                val = stack.pop()
                intervals[val[1]] = i - val[1]
            stack.append([temperatures[i],i])
        
        for i in range(n):
            result[i] = intervals[i]

        return result

        
        