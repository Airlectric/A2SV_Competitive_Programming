def isIncreasing(n,arr):
    indexSum = 0
    stackSum = 0

    for i in range(n):
        indexSum += i
        stackSum += arr[i]
        if indexSum > stackSum:
            return 'NO'
    
    return 'YES'
        
            
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(isIncreasing(n,arr))