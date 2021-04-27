from functools import lru_cache
d = 30
f = 30
target = 500
# Output: 222616187

def numRollsToTarget(d, f, target):
    @lru_cache(None)
    def dfs(t, d):
        if t == 0 and d == 0: return 1
        if d <= 0 or t <= 0: return 0
        return sum(dfs(t-i, d-1) for i in range(1, f+1))
        
    return dfs(target, d) % int(1e9 + 7)

print(numRollsToTarget(d, f, target))
