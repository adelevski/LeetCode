from collections import defaultdict

words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
# Output: ["mee", "aqq"]

# words = ["a", "b", "c"]
# pattern = "a"
# # Output: ["a", "b", "c"]



def findAndReplacePattern(words, pattern):
    
    def get_pattern(s):
        d = defaultdict(list)
        for i in range(len(s)):
            d[s[i]].append(i)
        return list(d.values())

    p = get_pattern(pattern)

    output = []
    for word in words:
        if get_pattern(word)==p:
            output.append(word)
        
    return output
        

print(findAndReplacePattern(words, pattern))


