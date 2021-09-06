from itertools import accumulate

stones = [5,3,1,4,2]
# Output: 6



def stoneGame(stones):
    N = len(stones)
    dp = [[0]*N for _ in range(N)]

    for i in range(N-2, -1, -1):
        total = stones[i]
        for j in range(i+1, N):
            total += stones[j]
            dp[i][j] = max(total-stones[i]-dp[i+1][j], total-stones[j]-dp[i][j-1])
    return dp[0][-1]

print(stoneGame(stones))


