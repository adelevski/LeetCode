from heapq import heapify, heappush, heappop

target = [9, 3, 5]
#        [1, 1, 1] x = 3 choose index 1
#        [1, 3, 1] x = 5 choose index 2
#        [1, 3, 5] x = 9 choose index 0
#        [9, 3, 5]
# Output = True

# target = [1, 1, 1, 2]
# #        [1, 1, 1, 1] x = 4 -> not possible
# # Output = False

# target = [8, 5]
# #        [1, 1] x = 2 choose index 1
# #        [1, 2] x = 3 choose index 0
# #        [3, 2] x = 5 choose index 1
# #        [3, 5] x = 8 choose index 0
# #        [8, 5]
# # Output = True

def isPossible(target):
    h = [-n for n in target]
    total = sum(target)
    heapify(h)
    while h[0] != -1:
        cand = -heappop(h)
        rest_of = total - cand
        if rest_of <= 0 or cand <= rest_of: return False
        prev = cand%rest_of
        heappush(h, -prev)
        total -= cand
        total += prev
    return True

print(isPossible(target))