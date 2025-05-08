class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        values = []
        n = len(position)
        stack = []

        for i in range(n):
            time = (target - position[i])/ speed[i]
            values.append((position[i],time))
        
        values.sort(key=lambda x:x[0])

        for i in range(n-1,-1,-1):

            if not stack or values[i][1] > stack[-1]:
                stack.append(values[i][1])
        
        return len(stack)

        