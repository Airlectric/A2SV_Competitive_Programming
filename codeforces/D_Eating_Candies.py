def numOfCandies(n,arr):
    left = 0
    right = n-1
    alice = 0
    bob = 0
    max_candies = 0

    while left <= right:

        if alice < bob:
            alice += arr[left]
            left += 1
        elif alice > bob:
            bob += arr[right]
            right -= 1
        else:
            max_candies = left + (n-right-1)
            alice += arr[left]
            left += 1
        
    if alice == bob:
        max_candies = left + (n-right-1)
            

    return max_candies


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(numOfCandies(n,arr))