def aliceBob(n,pref,suff):
    Bob = 0
    Alice = 0

    pref = pref[1:]

    for i in range(n):
        if pref[i] > suff[i]:
            Bob += 1
        else:
            Alice += 1

    return [Alice,Bob]


n = int(input())
arr = list(map(int,input().split()))

prefixSum = [0] * (n+1)
suffixSum = [0] * (n)
suffixSum[-1] = arr[-1]

for i in range(n):
    prefixSum[i+1] = prefixSum[i] + arr[i]

for i in range(n-2,-1,-1):
    suffixSum[i] = suffixSum[i+1] + arr[i]

result = aliceBob(n,prefixSum, suffixSum)
print(*result)





    
        
