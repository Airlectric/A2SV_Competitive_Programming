t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    min_idx = arr.index(min(arr))
    max_idx = arr.index(max(arr)) 

    if abs(arr[min_idx]-arr[min_idx]) + abs(arr[min_idx]-arr[max_idx]) == abs(arr[min_idx]-arr[max_idx]):
        print(*[min_idx+1,max_idx+1])
    
        
    

