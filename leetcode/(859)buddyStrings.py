
# 859. Buddy Strings


def buddyStrings(a, b):
    if len(a) != len(b):
        return False
    if a == b and len(set(a)) < len(a):
        return True
    differences = []
    for x in range(len(a)):
        if a[x] != b[x]:
            differences.append([a[x], b[x]])
    
    if len(differences) == 2 and differences[0] == differences[1][::-1]:
        return True



print(buddyStrings('ab', 'ba'))

# DID NOT KNOW ABOUT THIS PYTHON FUNCTIONALITY! THIS IS AMAZING!
alist = [1, 2, 3, 4, 5]

print(alist[::-1])