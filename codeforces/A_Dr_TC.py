from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    nums = str(input())

    count = Counter(nums)
    ans = 0

    for num in nums:
        if num == '1':
            ones = count['1']
            ans += (ones-1)
        else:
            ones = count['1']
            ans += (ones+1)
    
    print(ans)

