

# 387. First Unique Character in a String

def firstUniqChar(string):
    hashmap = {}
    for key in string:
        if key not in hashmap:
            hashmap.update({key: 1})
        else:
            hashmap[key] += 1
    for key in hashmap:
        if hashmap[key] == 1:
            print(key)
            return
    print("No non-repeating characters")

firstUniqChar('abcabcabcfggggg')
