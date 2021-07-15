


s = "egg"
t = "add"
# Output: true

# s = "foo"
# t = "bar"
# # Output: false

# s = "paper"
# t = "title"
# # Output: true

def isIsomorphic(s, t):
    N = len(s)
    d = {}
    d2 = {}
    for i in range(N):
        d.setdefault(s[i], [])
        d2.setdefault(t[i], [])
        d[s[i]].append(i)
        d2[t[i]].append(i)
    return list(d.values()) == list(d2.values())


print(isIsomorphic(s, t))