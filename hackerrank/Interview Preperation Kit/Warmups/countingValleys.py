


steps = 8
path = 'UDDDUDUU'

def countingValleys(steps, path):
    level = 0
    valleys = 0
    
    for s in range(steps):
        if path[s] == 'U':
            level += 1
        if path[s] == 'D':
            level -= 1
        if level == 0 and path[s] == 'U':
            valleys += 1
    return valleys


print(countingValleys(steps, path))


