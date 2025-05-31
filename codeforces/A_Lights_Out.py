def lightsOut(arr):
    state = [[1] * 3 for _ in range(3)]

    for i in range(3):
        for j in range(3):
            if arr[i][j] % 2 == 1:

                state[i][j] = 1 - state[i][j]

                if i-1 >= 0:
                    state[i-1][j] = 1 - state[i-1][j]
                if i+1 < 3:
                    state[i+1][j] = 1 - state[i+1][j]
                
                if j-1 >= 0:
                    state[i][j-1] = 1 - state[i][j-1]
                if j+1 < 3:
                    state[i][j+1] = 1 - state[i][j+1]
    return state

                
                

arr = [list(map(int, input().split())) for _ in range(3)]
for row in lightsOut(arr):
    print(''.join(map(str, row)))