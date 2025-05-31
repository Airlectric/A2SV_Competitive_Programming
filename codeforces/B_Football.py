def dangerous(arr):
    count = 0

    for i in range(len(arr)):
        count += 1

        if arr[i] != arr[i-1]:
            count = 1
            
        if count == 7:
            return 'YES'
        

    return 'NO'




arr = list(map(int,input().strip()))
print(dangerous(arr))

