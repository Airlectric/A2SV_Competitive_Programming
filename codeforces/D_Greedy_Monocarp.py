t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    chests = list(map(int, input().split()))

    chests.sort(reverse=True)

    might_have = 0
    min_have = 0

    i = 0
    might_have += chests[i]

    while  i < len(chests) and might_have <= k:
        min_have += chests[i]
        i += 1
        if i < len(chests):
            might_have += chests[i]

    
    print(k - min_have)

