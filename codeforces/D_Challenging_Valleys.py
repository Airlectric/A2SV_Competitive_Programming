
def isValley(n, arr):
    l = 0
    count = 0

    for r in range(n):
        while arr[l] != arr[r]:
            l += 1

        if (l == 0 or arr[l-1] > arr[l]) and (r==n-1 or arr[r] < arr[r+1]): 
            count += 1

    return 'YES' if count == 1 else 'NO'



t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(isValley(n,arr))