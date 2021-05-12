import sys


mat = [[1,0,1],[1,1,0],[1,1,0]]
# Output = 13

def numSubmat(mat):
    m = len(mat)
    n = len(mat[0])
    
    dp = [[0]*n for _ in range(m)]
    
    for i in range(m):
        for j in range(n-1, -1, -1):
            if mat[i][j] == 1:
                dp[i][j] += 1 + (dp[i][j+1] if j < n - 1 else 0)
    ans = 0
    
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                minW = sys.maxsize
                for k in range(i, m):
                    minW = min(minW, dp[k][j])
                    ans += minW
    return ans

print(numSubmat(mat))