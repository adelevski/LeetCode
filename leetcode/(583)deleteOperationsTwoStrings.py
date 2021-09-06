

# word1 = "sea"
# word2 = "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

# word1 = "leetcode"
# word2 = "etco"
# # Output: 4

word1 = "sea"
word2 = "ate"
# Output = 4

def minDistance(word1, word2):
    N = len(word1)
    M = len(word2)
    dp = [[0 for i in range(N+1)] for j in range(M+1)]
    for c in range(N+1):
        dp[0][c] = c
    for r in range(M+1):
        dp[r][0] = r
    for r in range(1, M+1):
        for c in range(1, N+1):
            if word1[c-1] != word2[r-1]:
                dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + 1
            else:
                dp[r][c] = dp[r-1][c-1]
    return dp[-1][-1]



print(minDistance(word1, word2))