
# STDIN       Function
# -----       --------
# 2           t = 2
# 5           n = 5
# 2 1 5 3 4   q = [2, 1, 5, 3, 4]
# 5           n = 5
# 2 5 1 3 4   q = [2, 5, 1, 3, 4]

q1 = [2, 1, 5, 3, 4]
q2 = [2, 5, 1, 3, 4]


def minimumBribes(q):
    swaps = 0
    for i in range(len(q)):
        if q[i]-(i+1) > 2:
            print("Too chaotic")
            return

        for j in range(max(0, q[i]-2), i):
            if q[j] > q[i]:
                swaps += 1
    print(swaps)

print(minimumBribes(q2))