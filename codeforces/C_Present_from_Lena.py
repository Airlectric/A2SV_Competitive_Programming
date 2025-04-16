n = int(input())

max_ = (n * 2) + 1

for i in range(max_):
    limit = i if i <= n else (2 * n)-i

    space = '  ' * (n - limit)

    pattern = list(range(limit+1)) + list(range(limit-1,-1,-1))

    str_pattern = ' '.join(map(str, pattern))

    print(space + str_pattern)



