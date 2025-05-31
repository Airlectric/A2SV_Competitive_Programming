n = int(input())
arr = list(map(int, input().split()))

coins = 0
negCount = 0
zeroCount = 0


for i in range(n):
    if arr[i] < 0:
        coins += abs(arr[i] + 1)
        negCount += 1
    elif arr[i] > 0:
        coins += arr[i] - 1
    else:
        coins += 1
        zeroCount += 1

if negCount % 2 == 1 and zeroCount == 0:
    coins += 2

print(coins)

        
           
