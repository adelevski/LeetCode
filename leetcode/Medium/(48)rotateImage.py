
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]


def rotate(matrix):
    N = len(matrix)
    for row in range(N):
        for number in range(row):
            matrix[row][number], matrix[number][row] = matrix[number][row],matrix[row][number]

    for row in matrix:
        row.reverse()
        
    print(matrix)

rotate(matrix)

