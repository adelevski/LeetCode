


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

# Naive approach
def triplets(a, b, c):
    A, B, C = len(a), len(b), len(c)
    print(f"Lens = {A}, {B}, {C}")
    aMin, bMin, cMin = min(a), min(b), min(c)
    print(f"Mins = {aMin}, {bMin}, {cMin}")
    aMax, bMax, cMax = max(a), max(b), max(c)
    print(f"Maxs = {aMax}, {bMax}, {cMax}")
    answer = 0
    d = {}
    newA = [a[val] for val in range(A) if a[val] <= bMax]
    newB = [b[val] for val in range(B) if b[val] >= aMin or b[val] >= cMin]
    newC = [c[val] for val in range(C) if c[val] <= bMax]
    print(f"new lists = {newA}, {newB}, {newC}")
    Anew, Bnew, Cnew = len(newA), len(newB), len(newC)
    print(f"new lens = {Anew}, {Bnew}, {Cnew}")
    for i in range(Anew):
        for j in range(Bnew):
            for k in range(Cnew):
                if newA[i] <= newB[j] and newB[j] >= newC[k] and (newA[i], newB[j], newC[k]) not in d:
                    answer += 1
                    d.setdefault((newA[i], newB[j], newC[k]), False)
                    d[(newA[i], newB[j], newC[k])] = True
    return answer

print(triplets(a, b, c))