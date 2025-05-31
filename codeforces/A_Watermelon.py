def divideWaterMelon(w):
    if w == 2:
        return 'NO'
    elif w % 2 == 0:
        return 'YES'
    else:
        return 'NO'


w = int(input())
print(divideWaterMelon(w))

