from heapq import heappop, heappush

courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
# Output = 3

def scheduleCourse(courses):
    courses.sort(key=lambda x: x[1])

    heap = []
    max_time = 0

    for time, end_time in courses:
        heappush(heap, -time)
        max_time += time
        if max_time > end_time:
            big_time = heappop(heap)
            max_time += big_time
        
    return len(heap)

print(scheduleCourse(courses))

