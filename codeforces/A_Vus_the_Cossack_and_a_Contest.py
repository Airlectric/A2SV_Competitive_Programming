n, k, m = map(int, input().split())

def fairshare(n,k,m):
    if k < n or m < n:
        return 'No'
    else:
        return 'Yes'
    
print(fairshare(n,k,m))