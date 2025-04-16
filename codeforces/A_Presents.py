n = int(input())
p_arr = list(map(int,input().split())) 

res = []

track = {}

for i in p_arr:
    track[i] = p_arr.index(i) + 1

for num in range(1,n+1):
    res.append(track[num])


print(*res)