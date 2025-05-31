def longGood(n,k,arr):
    left = 0
    longest = float('-inf')
    freq_visited = {}
    res = [1,1]

    for right in range(n):
        freq_visited[arr[right]] = freq_visited.get(arr[right],0) + 1

        while len(freq_visited) > k:
            freq_visited[arr[left]] -= 1
            if freq_visited[arr[left]] == 0:
                del freq_visited[arr[left]]
            left += 1
        
        length = right - left + 1

        if length > longest:
            longest = length
            res = [left+1,right+1]

    return res




n , k = map(int, input().split())
arr = list(map(int,input().split()))
result = longGood(n,k,arr)
print(*result)

