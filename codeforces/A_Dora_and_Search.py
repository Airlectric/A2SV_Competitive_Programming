def segmentExist(n,a):
    l = 0
    r = n-1
    low, high = 1,n
    while l<r:
        if a[l] == low: l += 1; low += 1
        elif a[l] == high: l += 1; high -= 1
        elif a[r] == low: r -= 1; low += 1
        elif a[r] == high: r -= 1; high -= 1
        else: break

    if l < r:
        return [l+1,r+1]
    else:
        return -1

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = segmentExist(n,arr) 

    if ans == -1:
        print(ans)
    else:
        print(*ans)

