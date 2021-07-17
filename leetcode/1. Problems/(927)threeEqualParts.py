
arr = [1,0,1,0,1]
# Output: [0,3]


def threeEqualParts(arr):
    n = len(arr)
    idxs = [i for i in range(n) if arr[i] == 1]
    m = len(idxs)

    if m == 0: return [0, 2]
    if m % 3 != 0: return [-1, -1]

    p1, p2 = idxs[0], idxs[m//3-1]
    p3, p4 = idxs[m//3], idxs[2*m//3-1]
    p5, p6 = idxs[2*m//3], idxs[-1]

    part1, part2, part3 = arr[p1:p2+1], arr[p3:p4+1], arr[p5:p6+1]

    l1 = p3 - p2 - 1
    l2 = p5 - p4 - 1
    l3 = n - p6 - 1

    if l3 > l2 or l3 > l1: return [-1, -1]

    return [p2 + l3, p4 + l3 + 1]


print(threeEqualParts(arr))