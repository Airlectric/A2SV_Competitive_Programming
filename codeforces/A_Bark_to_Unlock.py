def crackPassword(pwsd,n,words):
    if pwsd in words:
        return 'YES'
    
    start = set()
    end = set()

    for word in words:
        start.add(word[0])
        end.add(word[1])

    if pwsd[0] in end and pwsd[1] in start:
        return 'YES'

    return 'NO'



pswd = str(input())

n = int(input())

words = []
for _ in range(n):
    words.append(str(input()))

print(crackPassword(pswd,n,words))
