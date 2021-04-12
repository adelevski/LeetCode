

d = 2
a = [1, 2, 3, 4, 5]

# Using temp array 
def rotLeft(a, d):
    temp = []
    for i in range(d):
        temp.append(a[i])
    
    i = 0
    while (d < len(a)):
        a[i] = a[d]
        i += 1
        d += 1
    
    a = a[:i] + temp

    return a
#Time complexity: O(n) 
#Auxiliary Space: O(d)


print(rotLeft(a, d))


    
