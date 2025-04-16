t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(str, input().split()))

    word_chs = "".join(arr)

    if '101' in word_chs:
        print('NO')
    else:
        print('YES')







