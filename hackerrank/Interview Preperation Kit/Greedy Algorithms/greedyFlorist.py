

c = [1, 3, 5, 7, 9]
k = 3
# Output = 29


def getMinimumCost(k, c):
    c.sort(reverse=True)
    total = 0
    count = 1
    for i in range(len(c)):
        if i%k==0 and i!=0:
            count += 1
        total += count*c[i]
    return total

print(getMinimumCost(k, c))
