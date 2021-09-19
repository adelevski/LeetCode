from collections import defaultdict

wall = [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]

def leastBricks(wall):
    N = len(wall)
    c = defaultdict(int)
    for row in wall:
        prev = 0
        for b in row[:-1]:
            prev+=b
            c[prev]+=1
    if not c: return N
    return N-max(c.values())

print(leastBricks(wall))