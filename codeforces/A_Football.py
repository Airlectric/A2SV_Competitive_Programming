def isDangerous(arr):
    start = 0
    n = len(arr)

    for end in range(n):
        
        while arr[end] != arr[start]:
            start += 1
        
        if (end-start+1) >= 7:
            return 'YES'
    
    return 'NO'


arr = list(map(int,input().strip()))
print(isDangerous(arr))

