from collections import defaultdict


matrix = [[1,-1],[-1,1]]
target = 0

def numSubmatrixSumTarget(matrix, target):
    # 1 2 3 4 5 target = 7
    # 1 3 6 10 15 
    # {1, 3, 6}
    N,M =  len(matrix[0]),len(matrix)
    output = 0

    for r in matrix:
        for i in range(1, len(r)):
            r[i] += r[i-1]

    for start in range(N):
        for end in range(start, N):
            lookup = defaultdict(int)
            cumsum = 0
            lookup[0] = 1
            for k in range(M):
                cumsum += matrix[k][end]-(matrix[k][start-1] if start != 0 else 0)
                if cumsum-target in lookup:
                    output += lookup[cumsum-target]
                lookup[cumsum] += 1
        return output
    
print(numSubmatrixSumTarget(matrix, target))
