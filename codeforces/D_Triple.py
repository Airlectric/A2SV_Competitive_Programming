from collections import Counter

def triple(arr):
    numCount = Counter(arr)

    for num in arr:
        if numCount[num] >= 3:
            return num
    
    return -1



t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(input().split())
    print(triple(arr))