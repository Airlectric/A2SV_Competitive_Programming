def optimalDistance(arr):
    arr.sort()
    both = False

    if arr[1]-arr[0] != 0:
        arr[0] += 1
        if arr[1]-arr[0] != 0:
            arr[1] -= 1
    else:
        both = True
    
    if arr[2]-arr[1] != 0:
        arr[2] -= 1
        if both and arr[2]-arr[1] != 0:
            arr[0] += 1
            arr[1] += 1

    return (arr[1]-arr[0]) + (arr[2]-arr[1]) + (arr[2]-arr[0])

t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))
    print(optimalDistance(arr))