t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    def satisfies(n,k):
        if k <= n:
            if n % 2 == 0 and k % 2 == 0:
                return 'YES'
            elif n % 2 == 1 and k % 2 == 1:
                return 'YES'
            elif n % 2 == 0 and k % 2 == 1:
                return 'YES'
            elif n % 2 == 0 and k == 1:
                return 'YES'
            elif n % 2 == 1 and k % 2 == 0:
                return 'NO'
        else:
            return 'NO'

    print(satisfies(n,k))
        
