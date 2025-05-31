t = int(input())

for _ in range(t):
    n, x = map(int,input().split())

    arr = [i for i in range(n)]

    if x in arr:
        arr = arr[:x] + arr[x+1:] + [arr[x]]
    else:
        arr = arr[:x]
    
    print(*arr)
        