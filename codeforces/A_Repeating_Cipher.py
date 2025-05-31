def decrypt(n,arr):
    count = 0
    res = ""
    for i in range(n-1):
        stop = 0
        while stop < i+1:
            stop += 1
            count += 1
        res += arr[count-1]

        if count > n-1:
            break
    
    return res if res != "" else arr



n = int(input())
arr = input()
print(decrypt(n,arr))

