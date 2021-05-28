from collections import defaultdict

words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: "abcw" and "xtfn"



# My method
def maxProduct(words):
    N = len(words)
    output = 0
    for i in range(N):
        for j in range(N):
            if i==j or j<=i:
                continue
            else:
                if set(words[i]) & set(words[j]):
                    continue
                else:
                    output = max(output, (len(words[i])*len(words[j])))
    return output

# Timothy's method
def maxProduct(words):
    lookup = defaultdict(set)
    
    for w in words:
        lookup[w] = set(w)
    
    def dont_share(s,t):
        if lookup[s]&lookup[t]:
            return False
        return True
    
    mx = 0
    for i in words:
        for j in words:
            if dont_share(i,j):
                mx = max(mx, len(i)*len(j))
                
    return mx


print(maxProduct(words))
