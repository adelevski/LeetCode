

n = 7
c = [0, 0, 1, 0, 0, 1, 0]


def jumpingOnClouds(c):
    i = 0
    jumps = 0
    while i < n-1:
        if i+2 < n and c[i+2] == 0:
            i += 2
            jumps += 1
        elif i+1 < n and c[i+1] == 0:
            i += 1
            jumps += 1
    return jumps
        
print(jumpingOnClouds(c))