from functools import lru_cache


d = 30
f = 30
target = 500
# Output: 222616187

def numRollsToTarget(d, f, target):
    mod = 10 ** 9 + 7
    @lru_cache(maxsize=None)
    def dp(i, t):
        if i==0: return 1 if t == 0 else 0
        if t>f*i or t<i: return 0
        ans = 0
        for k in range(1, min(f, t) + 1):
            ans = (ans + dp(i-1, t-k)) % mod
        return ans
    return dp(d, target)

print(numRollsToTarget(d, f, target))
