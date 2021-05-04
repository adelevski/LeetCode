
s1 = 'SHINCHAN'
s2 = 'NOHARAAA'

# DP solution, too slow in Python 3, works fine with PyPy3
def commonChild(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[n][m]  

print(commonChild(s1, s2))
