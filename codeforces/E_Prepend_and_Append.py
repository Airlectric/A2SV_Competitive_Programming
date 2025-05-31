t = int(input())

for _ in range(t):
    n = int(input())
    bstr = str(input())

    count = 0
    left = 0
    right = n-1

    while left < right:
        if bstr[left] != bstr[right]:
            count += 2
        else:
            break
        left += 1
        right -= 1

    print(n-count)


