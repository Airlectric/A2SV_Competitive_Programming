def oneTwo(n, arr):
    prefixProduct = [0] * n

    prefixProduct[0] = arr[0]

    for i in range(1,n):
        prefixProduct[i] = prefixProduct[i-1] * arr[i]

    for i in range(n):
        if prefixProduct[i] == 0:
            if prefixProduct[-1] == 0:
                return i+1
        else:
            if prefixProduct[i] == prefixProduct[-1] // prefixProduct[i]:
                return i+1
    
    return -1


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(oneTwo(n,arr))