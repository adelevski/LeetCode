# index->	 1 2 3  4  5 6 7 8 9 10
# 	        [0,0,0, 0, 0,0,0,0,0, 0]
# 	        [3,3,3, 3, 3,0,0,0,0, 0]
# 	        [3,3,3,10,10,7,7,7,0, 0]
# 	        [3,3,3,10,10,8,8,8,1, 0]

n = 10
queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]

def arrayManipulation(n, queries):
    myList = [0]*n
    maxVal = 0
    cur = 0
    for query in queries:
        first = query[0] - 1
        second = query[1] - 1
        summand = query[2]
        myList[first] += summand
        if second+1 < n:
            myList[second+1] -= summand
    for val in myList:
        cur += val
        if cur > maxVal:
            maxVal = cur
    return maxVal

print(arrayManipulation(n, queries))


