nums = str(input())

res = ''

for i in range(len(nums)):
    if i == 0 and nums[i] == '9':
        res += nums[i]
        continue
    num = int(nums[i])
    if num > 4:
        res += str(9-num)
    else:
        res += nums[i]

print(int(res))