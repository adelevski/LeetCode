

from sortedcontainers import SortedList


class MedianFinder:

    def __init__(self):
        self.lst = SortedList()

    def addNum(self, num):
        self.lst.add(num)
    
    def findMedian(self):
        N = len(self.lst)
        if N % 2 == 0:
            return (self.lst[N//2] + self.lst[(N//2)-1]) / 2
        else:
            return self.lst[N//2]




obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.addNum(3)
obj.addNum(4)
param_2 = obj.findMedian()

print(param_2)




