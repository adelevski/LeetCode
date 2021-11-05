
n = 5
# Output: 2

# n = 8
# Output: 3

def arrangeCoins(n):
    ans = 0
    i = 1
    while n > 0:
        if n - i >= 0:
            ans += 1
        n -= i
        i += 1
    return ans


print(arrangeCoins(n))

