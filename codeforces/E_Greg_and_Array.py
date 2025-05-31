n , m, k = map(int,input().split())

arr = list(map(int, input().split()))

ops = [list(map(int, input().split())) for _ in range(m)]

queries = [list(map(int, input().split())) for _ in range(k)]

ops_dirr_arr = [0] * (m+2)

for x,y in queries:
    ops_dirr_arr[x] += 1
    ops_dirr_arr[y+1] -= 1

for i in range(1,m+1):
    ops_dirr_arr[i] += ops_dirr_arr[i-1]


diff_arr = [0] * (n+2)

for i in range(m):
    l,r,d = ops[i]
    times = ops_dirr_arr[i+1] * d
    diff_arr[l] += times
    diff_arr[r+1] -= times

for i in range(1,n+1):
    diff_arr[i] += diff_arr[i-1]
    arr[i-1] += diff_arr[i]

print(*arr)
