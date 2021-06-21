

numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

def generate(numRows):
    triangle = [[1]]
    for i in range(1, numRows):
        next_list = [1]
        for j in range(1, i):
            next_list.append(triangle[i-1][j-1]+triangle[i-1][j])
        next_list.append(1)
        triangle.append(next_list)
    return triangle



print(generate(numRows))