

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
# Output: True

# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbbaccc"
# # Output: False

# s1 = ""
# s2 = ""
# s3 = ""
# # Output: True

# Using recursion and memoization
def isInterleave(s1, s2, s3):
    N = len(s3)
    A,B = len(s1),len(s2)
    if A+B!=N: return False

    memo = {}
    def rec(i,j,k):
        if (i,j,k) in memo:
            return memo[(i,j,k)]
        #base case
        if i == A and j==B and k==N:
            return True
        b1,b2 = False,False
        if i<A and s1[i]==s3[k]:
            b1 = rec(i+1,j,k+1)
        if j<B and s2[j]==s3[k]:
            b2 = rec(i,j+1,k+1)
        memo[(i,j,k)] = b1 or b2
        return b1 or b2

    return rec(0,0,0)


print(isInterleave(s1, s2, s3))

