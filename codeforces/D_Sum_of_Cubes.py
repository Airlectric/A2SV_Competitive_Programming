def isCubeSum(x):
    n = int(x ** (1/3))

    a = set()

    val = 1
    while val**3 < x:
        a.add(val**3)
        val += 1
    
    for i in range(1,n+1):
        diff = x - i**3
        if diff in a:
            return 'YES'
    
    return 'NO'


t = int(input())

for _ in range(t):
    x = int(input())
    print(isCubeSum(x))