n = list(map(int, input().split('+')))

n.sort()

n = "+".join(map(str, n))

print(n)