# def maxTheorems(n,k,arr,times):
#     start = 0
#     max_ = float('-inf')
#     constant = 0
#     value = 0

    
#     for i in range(n):
#         if times[i] == 1:
#             constant += arr[i]

#     for end in range(n):

#         while (end - start + 1) > k:
#             if times[start] == 0:
#                 value -= arr[start]
#             start += 1

#         if times[end] == 0:
#             value += arr[end]

#         max_ = max(max_,value)

#     return max_ + constant




n, k = map(int, input().split())

arr = list(map(int, input().split()))
times = list(map(int, input().split()))
# print(maxTheorems(n,k,arr,times))



constant = 0
asleep = []

for i in range(n):
    if times[i] == 0:
        asleep.append(arr[i])
    else:
        asleep.append(0)

for i in range(n):
    if times[i] == 1:
        constant += arr[i]

for i in range(1,n):
    asleep[i] += asleep[i-1]

max_ = float('-inf')

for i in range(n):
    if i-k >= 0:
        sum_ = asleep[i] - asleep[i-k]
    else:
        sum_ = asleep[i]

    max_ = max(max_, sum_)
        
print(constant+max_)


