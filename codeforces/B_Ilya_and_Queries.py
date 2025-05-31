def countSame(x,y,prefixSum):
    return prefixSum[y] - prefixSum[x]

        
items = list(map(str, input().strip()))

q = int(input())

queries = [list(map(int,input().split())) for _ in range(q)]



n = len(items)
same = [0] * n

for i in range(1,n):
    same[i] = 1 if items[i] == items[i-1] else 0

prefixSum = [0] * (n+1)

for i in range(n):
    prefixSum[i+1] = prefixSum[i] + same[i]


for query in queries:
    print(countSame(query[0],query[1],prefixSum))