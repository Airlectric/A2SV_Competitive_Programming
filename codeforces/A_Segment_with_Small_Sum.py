n, s = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
lg_sq = 0
result = 0

for end in range(n):
    result += arr[end]
    while start < n and result > s:
        result -= arr[start]
        start += 1
    lg_sq = max(lg_sq, end-start+1)

print(lg_sq)

    