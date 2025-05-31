def maxValue(n,arr1,m,arr2):
    prefixSum = [0] * (n+1)
    
    for i in range(n):
        prefixSum[i+1] = prefixSum[i] + arr1[i]
    
    prefixSum2 = [0] * (m+1)
    
    for i in range(m):
        prefixSum2[i+1] = prefixSum2[i] + arr2[i]
    
    return max(0, (max(prefixSum)+max(prefixSum2)))


t = int(input())

for _ in range(t):
    n = int(input())
    arr1 = list(map(int, input().split()))
    m = int(input())
    arr2 = list(map(int, input().split()))
    print(maxValue(n,arr1,m,arr2))