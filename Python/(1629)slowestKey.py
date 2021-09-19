
from collections import defaultdict


releaseTimes = [9,29,49,50]
keysPressed = "cbcd"
# Output: "c"


def slowestKey(releaseTimes, keysPressed):
    d = defaultdict(int)
    d[keysPressed[0]] = releaseTimes[0]
    for i in range(1, len(keysPressed)):
        key = keysPressed[i]
        time = releaseTimes[i] - releaseTimes[i-1]
        if key in d.keys():
            d[key] = max(d[key], time)
        else:
            d[key] = time
    lst = [k for k in d.keys() if d[k] == max(d.values())]
    return max(lst)

print(slowestKey(releaseTimes, keysPressed))