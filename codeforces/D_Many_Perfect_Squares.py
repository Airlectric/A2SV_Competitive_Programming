import math 

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    max_ = max(arr)
    
    val  = (max_**0.5)+1 
    x_limit = (val * val) - max_

    num = 5

    for i in range(x_limit):
        

    print(math.isqrt(num))