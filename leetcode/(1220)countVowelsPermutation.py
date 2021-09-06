
n = 1
# Output: 5

def countVowels(n):
    a = e = i = o = u = 1
    MOD = 10**9 + 7
    for _ in range(n-1):
        a, e, i, o, u = (e + i + u) % MOD, (a + i) % MOD, (e + o) % MOD, i, (i + o) % MOD
    return (a + e + i + o + u) % MOD



print(countVowels(n))