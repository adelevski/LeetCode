
s1 = 'and'
s2 = 'art'
s3 = 'be'
s4 = 'cat'

def twoStrings(s1, s2):
    first = {}
    second = {}
    commonChars = False
    for char in s1:
        if char not in first:
            first[char] = 1
    for char in s2:
        if char not in second:  
            second[char] = 1
    for char in first:
        if char in second:
            return 'YES'
    return 'NO'

print(twoStrings(s3, s4))