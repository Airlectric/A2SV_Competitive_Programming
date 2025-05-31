from collections import Counter

def triple(n,arr):
    detect = Counter()

    for i in range(n):
        detect[arr[i]] += 1

        if detect[arr[i]] >= 3:
            return arr[i]
    
    return -1



t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(triple(n,arr))

