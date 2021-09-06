
words = ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: One of the longest word chain is "a","ba","bda","bdca".


words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
# Output: 5

def longestStrChain(words):
    s = set(words)
    memo = {}

    def rec(word):
        if word not in s: return 0
        if word in memo:
            return memo[word]
        else:
            N = len(word)
            mx = 0
            for i in range(N):
                mx = max(mx, rec(word[:i]+word[i+1:])+1)
            memo[word] = mx
        return mx
    for w in words:
        rec(w)
    return max(memo.values())

print(longestStrChain(words))