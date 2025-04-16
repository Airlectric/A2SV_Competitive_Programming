t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    result = [0] * n

    max_idx = arr.index(max(arr))

    sorted_arr = sorted(arr)

    for i in range(n):
        if arr[i] < arr[max_idx]:
            result[i] = arr[i]- arr[max_idx]
    
    result[max_idx] = arr[max_idx] - sorted_arr[-2]
    
    print(*result)