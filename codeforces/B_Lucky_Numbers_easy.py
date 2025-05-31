from collections import Counter

def superLucky(num):
    mock = ['4','4','7']
    detect = Counter(mock)
    num_str = ''
    while detect['4'] != detect['7'] or len(num_str) != detect['4']+detect['7']:

        num_str = str(num)

        detect = Counter(map(str,num_str))

        num += 1

    return num-1



num = int(input())

print(superLucky(num))