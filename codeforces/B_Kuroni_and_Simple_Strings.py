arr = list(map(str, input().strip()))
n = len(arr)

left = 0
right = n-1
ops = 0
res = []

while left < right:
    if arr[left] == '(' and arr[right] == ')':
        ops += 1
        res.append(left+1)
        res.append(right+1)
        left += 1
        right -= 1

    if arr[left] != '(' :
        left += 1
    
    if arr[right] != ')':
        right -= 1

res.sort()


if ops > 0:
    print(1)
    print(ops * 2)
    print(*res)
else:
    print(0)



    