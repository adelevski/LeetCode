
from heapq import heappush, heappop
from sortedcontainers import SortedList

# Using SortedList
class MedianFinder:

    def __init__(self):
        self.lst = SortedList()

    def addNum(self, num):
        self.lst.add(num)
    
    def findMedian(self):
        N = len(self.lst)
        if N % 2 == 0:
            return (self.lst[N//2] + self.lst[(N//2)-1]) / 2
        return self.lst[N//2]



# Using min and max heap
class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap, -num)
        heappush(self.minHeap, -heappop(self.maxHeap))
        if len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        return (-self.maxHeap[0] + self.minHeap[0]) / 2




