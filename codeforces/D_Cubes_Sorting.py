t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    def swapE(n,arr):
        for j in range(n-1):
            if  arr[j] <= arr[j+1]:
                return 'YES'
        return 'NO'
    
    print(swapE(n,arr))
