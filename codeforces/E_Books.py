def maxBooks(n,t,arr):
    t_tot = 0
    start = 0
    min_b = 0
    
    for end in range(n):
        t_tot += arr[end]

        while t_tot > t:
            t_tot -= arr[start]
            start += 1
        
        min_b = max(min_b,(end - start +1))

    return min_b



n, t = map(int, input().split())

arr = list(map(int, input().split()))

print(maxBooks(n,t,arr))

