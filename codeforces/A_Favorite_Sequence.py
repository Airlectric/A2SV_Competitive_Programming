t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    i = 0
    j = n-1
    result = []

    while i < j:
        result.append(arr[i])
        result.append(arr[j])
        i += 1
        j -= 1
    
    if n % 2 == 1:
        result.append(arr[i])

    print(*result)


