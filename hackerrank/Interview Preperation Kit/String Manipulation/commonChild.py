
s1 = 'SHINCHAN'
s2 = 'NOHARAAA'

# DP solution, too slow without optimization
# def commonChild(s1, s2):
#     n = len(s1)
#     m = len(s2)
#     dp = [[0 for i in range(n+1)] for j in range(m+1)]
#     for i in range(1, n+1):
#         for j in range(1, m+1):
#             if s1[i-1] == s2[j-1]:
#                 dp[i][j] = dp[i-1][j-1] + 1
#             else:
#                 dp[i][j] = max(dp[i][j-1], dp[i-1][j])
#     return dp[n][m]  

# DP solution, with optimization
def commonChild(s1, s2):
    n = len(s1)
    m = len(s2)
    start = 1
    n_end = n
    m_end = m
    while (start <= n_end and start <= m_end and s1[start] == s2[start]):
        start += 1
    while (start <= n_end and start <= m_end and s1[n_end-1] == s2[m_end-1]):
        n_end -= 1
        m_end -= 1
    dp = [[0 for i in range(start-1, n_end+1)] for j in range(start-1, m_end+1)]
    for i in range(start, n_end+1):
        for j in range(start, m_end+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[n_end][m_end]   
    

# Not working,will finish in the am
# print(commonChild(s1, s2))
