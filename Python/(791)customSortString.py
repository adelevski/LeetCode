

order = "cba"
str = "abcd"
# Output: "cbad"



def customSortString(order, str):
    d = {}
    output = ''
    for char in str:
        d.setdefault(char, 0)
        d[char] += 1
    for i in range(len(order)):
        if order[i] in d.keys() and d[order[i]] > 0:
            output += order[i] * d[order[i]]
            d[order[i]] = 0
    for char, num in d.items():
        output += char * num

    return output



print(customSortString(order, str))