matrix = [[3,2,1,4],[6,7,11,9],[0,12,8,15],[3,-1,20,-2]]

def twoDPrefixSum(mat):
    m = len(mat)
    n = len(mat[0])

    prefixSumMatrix = [[0] * (n+1) for _ in range(m+1)]

    for i in range(m):
        for j in range(n):
            prefixSumMatrix[i+1][j+1] = mat[i][j] + prefixSumMatrix[i][j+1] \
                  + prefixSumMatrix[i+1][j] - prefixSumMatrix[i][j]
    
    return prefixSumMatrix


print(twoDPrefixSum(matrix))

                
