
mat = [[1,2],[3,4]]
r = 1
c = 4
# Output: [[1,2,3,4]]



def getCell(mat):
    for row in mat:
        for cell in row:
            yield cell
def matrixReshape(mat, r, c):
    gen = getCell(mat)
    return [[next(gen) for _ in range(c)] for _ in range(r)] if len(mat) * len(mat[0]) == r * c else mat


print(matrixReshape(mat, r, c))