t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    i = 0
    j = n-1

    arr.sort()
    result = 0
    total = 0


    while i<j:
        total = arr[j] - arr[i]
        result += total

        i += 1
        j -= 1

    print(result)
       