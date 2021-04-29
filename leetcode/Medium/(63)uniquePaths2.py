obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output = 2

def uniquePathsWithObstacles(obstacleGrid):
    N, M = len(obstacleGrid[0]), len(obstacleGrid)
    dp = [[0 for _ in range(N)] for _ in range(M)]
    #first row
    for c in range(N):
        if obstacleGrid[0][c] == 1: break
        dp[0][c] = 1

    for r in range(M):
        if obstacleGrid[r][0] == 1: break
        dp[r][0] = 1

    for r in range(1, M):
        for c in range(1, N):
            if obstacleGrid[r][c] == 1: continue
            dp[r][c] = dp[r-1][c] + dp[r][c-1]

    return dp[-1][-1]

print(uniquePathsWithObstacles(obstacleGrid))

