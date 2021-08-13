from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


def groupAnagrams(strs):
    t = defaultdict(list)
    for s in strs:
        t["".join(sorted(s))].append(s)
    return t.values()


print(groupAnagrams(strs))