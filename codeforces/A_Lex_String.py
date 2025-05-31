def lexi(n,m,k,a,b):
    a.sort()
    b.sort()
    cnt_a = 0
    cnt_b = 0

    i = j = 0

    c = []

    while i < n and j < m:
        if (a[i] < b[j] and cnt_a < k) or cnt_b == k:
            c.append(a[i])
            i += 1
            cnt_a += 1
            cnt_b = 0
        else:
            c.append(b[j])
            j += 1
            cnt_b += 1
            cnt_a = 0
    
    return ''.join(c)


t = int(input())

for _ in range(t):
    n,m,k = map(int,input().split())
    a = list(map(str, input().strip()))
    b = list(map(str, input().strip()))
    print(lexi(n,m,k,a,b))