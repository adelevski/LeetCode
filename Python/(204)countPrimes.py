
# n = 10
# # Output = 4

n = 120
# Output = 30


# This algorithm is called Sieve of Eratosthenes
def countPrimes(n):
    if n == 0 or n == 1: return 0
    primes = [1]*n
    primes[0], primes[1] = 0, 0

    i = 2
    while i < n:
        tmp = i
        if primes[i]:
            tmp+=i
            while tmp<n:
                primes[tmp] = 0
                tmp += i
        i += 1
    return sum(primes)

print(countPrimes(n))