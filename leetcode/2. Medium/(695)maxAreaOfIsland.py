

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6

def maxArea(grid):
    M,N = len(grid),len(grid[0])

    def dfs(r,c):
        #inbounds and 1?
        if 0<=r<M and 0<=c<N and grid[r][c] == 1:
            grid[r][c] = 0
            return 1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)
        else:
            return 0
    output = 0
    for r in range(M):
        for c in range(N):
            output = max(output, dfs(r,c))
    return output

    
print(maxArea(grid))