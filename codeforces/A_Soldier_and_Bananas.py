def howMuchToBorrow(k,n,w):
    bananaCost = 0
    for i in range(1,w+1):
        bananaCost += k * i
 
    return max(0, bananaCost - n)


k, n, w = map(int, input().split())
print(howMuchToBorrow(k,n,w))

