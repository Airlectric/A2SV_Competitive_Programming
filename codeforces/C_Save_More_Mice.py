def numOfMice(n,k,micepos):
    micepos.sort(reverse=True)

    saved = 0
    cat_pos = 0

    for pos in micepos:
        runtime = n - pos
        if cat_pos + runtime < n:
            saved += 1
            cat_pos += runtime
    return saved


t = int(input())

for _ in range(t):
    n,k = map(int, input().split())
    micepos = list(map(int,input().split()))
    print(numOfMice(n,k,micepos))
