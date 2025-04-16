n = int(input())
arr = list(map(int, input().split()))

result = []

sum_of_arr = sum(arr)

for i in range(n):
    average = ((sum_of_arr - arr[i])/(n-1))
    if average == arr[i]:
        result.append(i+1)

print(len(result))
print(*result)