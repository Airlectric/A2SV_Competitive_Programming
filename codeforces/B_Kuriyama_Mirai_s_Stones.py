def stoneAns(type_,l,r):
    if type_ == 1:
        return prefixSum1[r] - prefixSum1[l-1]
    else:
        return prefixSum2[r] - prefixSum2[l-1]


n = int(input())
arr = list(map(int, input().split()))
t = int(input())

prefixSum1 = [0] * (n+1)

for i in range(n):
    prefixSum1[i+1] = prefixSum1[i] + arr[i]

arr2 = sorted(arr)

prefixSum2 = [0] * (n+1)

for i in range(n):
    prefixSum2[i+1] = prefixSum2[i] + arr2[i]

for _ in range(t):
    type_,l,r = map(int,input().split())
    print(stoneAns(type_,l,r))