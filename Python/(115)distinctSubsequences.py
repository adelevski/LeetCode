s = "rabbbit"
t = "rabbit"
# Output: 3

s = "babgbag"
t = "bag"
# Output: 5


def numDistinct(s, t):
    #@lru_cache(None) # To speed things up
    def dp(i,j):
        if i == -1: return j == -1
        if j == -1: return j == -1
        return dp(i-1, j) + (s[i] == t[j]) * dp(i-1, j-1)

    return dp(len(s) - 1, len(t) - 1)




print(numDistinct(s, t))