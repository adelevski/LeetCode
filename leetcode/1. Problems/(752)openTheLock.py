from collections import defaultdict, deque

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
# Output: 6

def openLock(deadends, target):
    nums = []
    deadends = set(deadends)
    if "0000" in deadends: return -1

    q = deque([("0000", 0)])
    visited = set()
    while q:
        cand,steps = q.popleft()
        if cand == target: return steps
        for i in range(4):
            for digit in [((int(cand[i])+1)%10),((int(cand[i])-1)%10)]:
                nx = cand[:i] + str(digit)+cand[i+1:]
                if nx not in deadends and nx not in visited:
                    visited.add(nx)
                    q.append((nx, steps+1))
    return -1


print(openLock(deadends, target))