from collections import defaultdict

# arr = [1, 3, 9, 9, 27, 81]
# r = 3

# arr = [1, 5, 5, 25, 125]
# r = 5

arr = [1, 2, 2, 4]
r = 2

def countTriplets(arr, r):
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    count = 0
    for i in reversed(arr):
        if i*r in d2:
            count += d2[i*r]
        if i*r in d1:
            d2[i] += d1[i*r]
        d1[i] += 1
    return count
                        
print(countTriplets(arr, r))