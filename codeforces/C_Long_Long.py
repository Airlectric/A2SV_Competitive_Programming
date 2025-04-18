t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    j = 0
    result = 0
    operations = 0
    in_negative = False

    while j < n:
        if arr[j] < 0:
            result += abs(arr[j])
            if not in_negative:
                operations += 1
                in_negative = True
            j += 1
        elif arr[j] > 0:
            result += arr[j]
            in_negative = False
            j+=1
        else:
            j+=1


    print(result,operations)

