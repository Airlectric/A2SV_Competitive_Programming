def max_teams(a,b):
    low = 0 
    high = min(a,b,(a+b)//4)
    ans = 0

    while low <= high:
        mid = low + (high - low) // 2

        if a >= mid and b >= mid and (a+b) >= 4 * mid:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans 



t = int(input())

for _ in range(t):
    a, b = map(int,input().split())
    print(max_teams(a,b))