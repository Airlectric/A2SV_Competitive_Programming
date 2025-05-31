def sumOfFree(n,x,y,prefixSum):
    sum_ = prefixSum[n-x+y] - prefixSum[n-x]
    return sum_ 



n, q = map(int, input().split())

items = list(map(int, input().split()))

queries = [list(map(int,input().split())) for _ in range(q)]

items.sort()

prefixSum = [0] * (n+1)

for i in range(n):
    prefixSum[i+1] = prefixSum[i] + items[i]

for query in queries:
    print(sumOfFree(n,query[0],query[1],prefixSum))




