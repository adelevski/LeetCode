from itertools import permutations

# Given an array of strings words, return the smallest string that contains each string in words as a substring. 
# If there are multiple valid strings of the smallest length, return any of them.
# You may assume that no string in words is a substring of another string in words.

words = ["catg","ctaagt","gcta","ttca","atgcatc"]
# Output: "gctaagttcatgcatc"

def shortest(words):
    N = len(words)
    cost = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(min(len(words[i]), len(words[j])),-1,-1):
                if words[i][-k:]==words[j][:k]:
                    cost[i][j] = k
                    break
    dp = [[(float('inf'),"")]*N for _ in range(1<<N)]
    for i in range(N):
        dp[1<<i][i] = (len(words[i]), words[i])
    for bitmask in range(1<<N):
        bits = [j for j in range(N) if bitmask & (1<<j)]
        for add, src in permutations(bits,2):
            cand = dp[bitmask^(1<<add)][src][1] + words[add][cost[src][add]:]
            dp[bitmask][add] = min(dp[bitmask][add],(len(cand),cand))
    return min(dp[-1])[1]

print(shortest(words))

