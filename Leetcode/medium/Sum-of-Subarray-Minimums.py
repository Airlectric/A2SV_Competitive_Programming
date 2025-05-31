class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        # computing previous less element
        stack1 = []
        PLE = [0] * n

        for i in range(n):
            while stack1 and arr[stack1[-1]] >= arr[i]:
                stack1.pop()

            PLE[i] = stack1[-1] if stack1 else -1
            stack1.append(i)

        # computing next less element
        stack2 = []
        NLE = [0] * n

        for i in range(n-1,-1,-1):
            while stack2 and arr[stack2[-1]] > arr[i]:
                stack2.pop()
            
            NLE[i] = stack2[-1] if stack2 else n
            stack2.append(i)
        
        total = 0

        for i in range(n):
            prev = i - PLE[i]
            next = NLE[i] - i
            occurances = prev * next
            total = total + (occurances*arr[i])
        
        return total % MOD

        