from heapq import heappop, heappush


target = 1
startFuel = 1
stations = []
# Output: 0

target = 100
startFuel = 1
stations = [[10,100]]
# Output: -1

target = 100
startFuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]
# Output: 2

def minStops(target, startFuel, stations):
    h = []
    output = 0
    prev = 0

    fuel = startFuel
    for distance, gas in stations+[(target, 0)]:
        fuel -= (distance-prev)
        while h and fuel < 0:
            fuel += -heappop(h)
            output += 1
        if fuel < 0: return -1
        heappush(h, -gas)
        prev = distance

    return output



print(minStops(target, startFuel, stations))