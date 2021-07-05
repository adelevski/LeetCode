
mat = [[1,2],[3,4]]
r = 1
c = 4
# Output: [[1,2,3,4]]


def matrixReshape(mat, r, c):
    oneD = []
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            oneD.append(mat[r][c])
    
    output = []
    for i in range(len(oneD)):
        
        output.append(tmpRow)

    return output


print(matrixReshape(mat, r, c))