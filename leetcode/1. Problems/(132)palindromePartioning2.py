
s = "aab"
# Output: 1

s = "a"
# Output: 0

s = "ab"
# Output: 1





def minCut(s):
    n = len(s)
        
    @lru_cache(None)
    def isPalindrome(l, r):  # l, r inclusive
        if l >= r: return True
        if s[l] != s[r]: return False
        return isPalindrome(l+1, r-1)
    
    @lru_cache(None)
    def dp(i):  # s[i..n-1]
        if i == n:
            return 0
        ans = math.inf
        for j in range(i, n):
            if (isPalindrome(i, j)):
                ans = min(ans, dp(j+1) + 1)
        return ans
    
    return dp(0) - 1



print(minCut(s))