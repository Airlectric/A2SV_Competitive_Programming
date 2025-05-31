def findBishop(board):
    for i in range(7):
        for j in range(1,7):
            if (board[i][j] == "#" and
                board[i-1][j-1] == "#" and
                board[i+1][j+1] == "#" and
                board[i+1][j-1] == "#" and
                board[i-1][j+1] == "#"):
                return [i+1, j+1]
            

t = int(input())

for _ in range(t):
    
    board = []

    while True:
        line = input()
        if line.strip():
            board.append(line.strip())
            break
    
    for _ in range(7):
        board.append(input().strip())

    result=findBishop(board)
    print(*result)