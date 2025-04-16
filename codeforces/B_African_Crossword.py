m, n = map(int, input().split())

mat = [list(input().strip()) for _ in range(m)]

result = ""

def checkRow(element,mat,n,row):
    count = 0
    for j in range(n):
        if element == mat[row][j]:
            count += 1
    return count


def checkCol(element,mat,m,col):
    count = 0
    for i in range(m):
        if element == mat[i][col]:
            count += 1
    return count


for i in range(m):
    for j in range(n):
        if checkRow(mat[i][j],mat,n,i) < 2 and checkCol(mat[i][j],mat,m,j) < 2:
            result += mat[i][j]

               
print(result)