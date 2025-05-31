def isEnough(n,arr,k,h):
    damage = 0
    for i in range(n-1):
        damage += min(k, arr[i+1] - arr[i])
    damage += k

    return damage >= h

def mink(n,h,arr):
    left = 1
    right = h
    res = 0

    while left <= right:
        mid = left + (right-left) // 2

        if isEnough(n,arr,mid,h):
            right = mid - 1
            res = mid
        else:
            left = mid + 1
    
    return res


t = int(input())

for _ in range(t):
    n, h = map(int, input().split())
    arr = list(map(int, input().split()))
    print(mink(n,h,arr))