
# s = 'AABAAB'
# # Output = 2

# s = 'ABABABAB'
# # Output = 0

s = 'AAABBB'
# Output = 4

def alternatingCharacters(s):
    N = len(s)
    output = 0
    for i in range(1, N):
        if s[i] == s[i-1]:
            output += 1
    return output


print(alternatingCharacters(s))