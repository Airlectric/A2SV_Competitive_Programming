def stringIntersect(a,b,c,d):
    compare = [a,b]
    compare.sort()

    if (compare[0] <= c <= compare[1]) != (compare[0] <= d <= compare[1]):
        return 'YES'
    else:
        return 'NO'
    

t = int(input())

for _ in range(t):
    a,b,c,d = map(int, input().split())
    print(stringIntersect(a,b,c,d))
    
