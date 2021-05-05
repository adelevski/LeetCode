


a = [1, 3, 5]
b = [2, 3]
c = [1, 2, 3]
# Output = 8

# a = [1, 4, 5]
# b = [2, 3, 3]
# c = [1, 2, 3]
# # Output = 5

# a = [1, 3, 5, 7]
# b = [5, 7, 9]
# c = [7, 9, 11, 13]
# # Output = 12

# Brilliat approach where you have a couple nested loops, 
# where you iterate over valid ints in a and c for each b, 
# then multiply the number of iterations and add to total
def triplets(a, b, c):
    a = list(sorted(set(a)))
    b = list(sorted(set(b)))
    c = list(sorted(set(c)))

    a1, b1, c1, ans = 0, 0, 0, 0

    while b1 < len(b):
        while a1 < len(a) and a[a1] <= b[b1]:
            a1 += 1
        while c1 < len(c) and c[c1] <= b[b1]:
            c1 += 1
        ans += a1 * c1
        b1 += 1
    return ans

print(triplets(a, b, c))