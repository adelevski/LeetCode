
# a = 'fcrxzwscanmligyxyvym'
# b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'
a = 'abc'
b = 'dcf'

def makeAnagram(a, b):
    output = 0
    chars = {}
    for char in a:
        chars.setdefault(char, [0, 0])
        chars[char][0] += 1
    for char in b:
        chars.setdefault(char, [0, 0])
        chars[char][1] += 1
    for char in chars:
        big = max(chars[char])
        small = min(chars[char])
        output += (big-small)
    return output

print(makeAnagram(a, b))
