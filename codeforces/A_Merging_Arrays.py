n, m = map(int,input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

pt1 = 0
pt2 = 0

new_arr = []

while pt1 < n and pt2 < m:
    if arr1[pt1] <= arr2[pt2]:
        new_arr.append(arr1[pt1])
        pt1 +=1
    else:
        new_arr.append(arr2[pt2])
        pt2 += 1


new_arr.extend(arr1[pt1:])
new_arr.extend(arr2[pt2:])


print(*new_arr)
