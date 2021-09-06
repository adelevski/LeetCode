n = 243

# Trivial loop solution
def isPowerOfThree(n):
    if n <= 0: return False
    x, i = 1, 0
    while x<=n:
        if x==n: return True
        i+=1
        x=3**i
    return False

# Loop-less solution given constraints
def powerOfThree(n):
    mx = 3**19
    return n>0 and mx%n==0

print(powerOfThree(n))