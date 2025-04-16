t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    max_ = max(arr)

    robot_count = [0] * (max_+1)

    for i in range(n):
        robot_count[arr[i]] += 1

    nrc = len(robot_count)
    count = 0

    check = True

    while count < nrc and check:
        if count+1 < nrc and robot_count[count] < robot_count[count+1]:
            check = False
            print('NO')
        count += 1
        if count == nrc:
            print('YES')
            check = False
    
    
        
    
    
            


