n = int(input())

distinct = n
distinct_str = []

while len(set(distinct_str)) != 4:
    distinct += 1
    distinct_str = str(distinct)


print(distinct)