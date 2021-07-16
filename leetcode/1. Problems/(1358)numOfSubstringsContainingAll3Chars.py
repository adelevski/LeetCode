
s = 'abcabc'
# Output: 10


def numOfSubstrings(s):
    dc = {}
    i = 0
    ln = len(s)
    res = 0
    for j in range(ln):
        dc.setdefault(s[j], 0)
        dc[s[j]]+=1
        try:
            while dc['a'] > 0 and dc['b'] > 0 and dc['c'] > 0:
                res += ln - j
                dc[s[i]] -= 1
                i += 1
        except KeyError:
            continue
            
    return res
    


print(numOfSubstrings(s))