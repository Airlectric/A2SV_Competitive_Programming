def isSquare(word):
    n = len(word)

    i = 0
    j = n-1

    while i < j:
        len_sq = len(word[:i+1])
        if word[:i+1] == word[j:] and (len_sq*2) == n:
            return 'YES'
        else:
            i += 1
            j -= 1
    
    return 'NO'



t = int(input())

for _ in range(t):
    word = str(input())

    print(isSquare(word))