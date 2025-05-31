from collections import defaultdict

def countGood(n,arr):
    seenBefore = defaultdict(int)
    count = 0
    prefixSumR = 0
    seenBefore[0] = 1

    for i in range(n):
        prefixSumR += arr[i]
        diff = prefixSumR - (i+1)
        if diff in seenBefore:
            count += seenBefore[diff]
            seenBefore[diff] += 1
        else:
            seenBefore[diff] += 1
    
    return count




t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().strip()))
    print(countGood(n,arr))