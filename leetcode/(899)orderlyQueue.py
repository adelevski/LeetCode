

s = "cba"
k = 1
# Output: "acb"


def orderlyQueue(s, k):
    if k > 1:
        return "".join(sorted(s))
    else:
        lst = []
        for i in range(len(s)):
            lst.append(s[i:] + s[:i])
        return min(lst)


print(orderlyQueue(s, k))