def infrontOf(arr):
    timur = arr[0]
    arr.sort()
    timur_idx = arr.index(timur)

    return len(arr[timur_idx+1:])

t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))
    print(infrontOf(arr))
    