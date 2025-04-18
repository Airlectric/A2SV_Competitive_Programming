from collections import defaultdict
import math

def cnt_squares(arr,n):
    track_k = defaultdict(int)
    cnt = 0
    max_ = 1


    for i in range(n):
        for j in range(i+1,n):
            d = arr[j]-arr[i]

            for f in range(1,math.isqrt(d)+1):
                if d % f:
                    continue
                for g in (f, d//f):
                    if (g-f) % 2:
                        continue
                    p = (g-f) // 2
                    if p < 0:
                        continue
                    k = p*p - arr[i]
                    if k < 0:
                        continue


                    track_k[k] = 0
    
    for k in track_k.keys():
        cnt = 0
        for ai in arr:
            x = ai + k
            t = math.isqrt(x)
            if t*t == x:
                cnt += 1
        max_ = max(max_, cnt)

    return max_

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(cnt_squares(arr,n))

    