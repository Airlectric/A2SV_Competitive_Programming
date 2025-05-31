class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        n = len(beans)
        beans.sort()
        min_beans = float('inf')
        prefixSum = [0] * (n+1)

        for i in range(n):
            prefixSum[i+1] = prefixSum[i] + beans[i]
        
        for i in range(n):
            diff = prefixSum[i] + (prefixSum[-1] - prefixSum[i+1] \
             -((n-(i+1)) * beans[i]))

            if beans[i] != beans[i-1]:
                min_beans = min(min_beans, diff)

        return min_beans if min_beans != float('inf') else 0




        

        
        