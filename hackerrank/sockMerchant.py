
n = 7
ar = [1, 2, 1, 1, 3, 2, 2, 2, 2]

def sockMerchant(n, ar):
    hashmap = {}
    for _ in ar:
        if _ in hashmap:
            hashmap[_] += 1
        else:
            hashmap[_] = 1
    pairs = 0
    for _ in hashmap:
        temp = hashmap[_] // 2
        pairs += temp
    return pairs

print(sockMerchant(n, ar))