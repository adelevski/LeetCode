
# matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


def setZeroes(matrix):
    R, C = len(matrix), len(matrix[0])
    rows, cols = set(), set()
    for r in range(R):
        for c in range(C):
            if matrix[r][c] == 0:
                cols.add(c)
                rows.add(r)
    for r in range(R):
        for c in range(C):
            if r in rows or c in cols:
                matrix[r][c] = 0
    return matrix

print(setZeroes(matrix))