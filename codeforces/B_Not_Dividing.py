def notDividing(n,arr):
    ops = 0

    if arr[0] == 1:
        arr[0] += 1
        ops += 1

    for i in range(1,n):
        if arr[i] == 1:
            arr[i] += 1
            ops += 1
        
        if arr[i] % arr[i-1] == 0:
            arr[i] += 1
            ops += 1

    return arr

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(*notDividing(n,arr))