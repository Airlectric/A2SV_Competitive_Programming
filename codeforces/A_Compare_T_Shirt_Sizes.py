def compareTshirt(a,b):
    val = {'S':-1, 'M':1, 'L':10, 'X':2}

    vala = 0
    valb = 0
    for i in range(len(a)-1,-1,-1):
        if a[i] == 'X':
            vala *= val[a[i]]
        else:
            vala += val[a[i]]

    for i in range(len(b)-1,-1,-1):
        if b[i] == 'X':
            valb *= val[b[i]]
        else:
            valb += val[b[i]]

    if vala > valb:
        return '>'
    elif vala < valb:
        return '<'
    else:
        return '='


t = int(input())

for _ in range(t):
    a, b = map(str, input().split())
    print(compareTshirt(a,b))