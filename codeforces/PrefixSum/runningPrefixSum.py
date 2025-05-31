arr = [1,3,5,6,9,-1,6,-4,8]

def exclusivePrefixSum(arr):
    n = len(arr)
    prefixSum = [0] * (n+1)

    for i in range(n):
        prefixSum[i+1] = prefixSum[i] + arr[i]

    return prefixSum


print(exclusivePrefixSum(arr))