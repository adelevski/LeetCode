from collections import defaultdict

s = "abcde"
words = ["a","bb","acd","ace"]
# Output: 3

s = "dsahjpjauf"
words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# Output: 2

def numMatch(s, words):
    lookup = defaultdict(list)
    output = 0

    for i,c in enumerate(s):
        lookup[c].append(i)

    def bs(lst,i):
        l,r = 0,len(lst)
        while l<r:
            mid = (l+r)//2
            if i < lst[mid]:
                r = mid
            else:
                l = mid+1
        return l

    for w in words:
        prev = -1
        found = True
        for c in w:
            tmp = bs(lookup[c], prev)
            if tmp == len(lookup[c]):
                found = False
                break
            else:
                prev = lookup[c][tmp]
        if found:
            output += 1

    return output




print(numMatch(s, words))