

# boxTypes = [[1,3],[2,2],[3,1]]
# truckSize = 4
# # Output: 8

boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
# Output: 91

def maxUnits(boxTypes, truckSize):
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    
    cap = 0

    for box,unit in boxTypes:
        if truckSize >= box:
            truckSize -= box
            cap += box*unit
        else:
            cap += truckSize*unit
            break
    return cap


print(maxUnits(boxTypes, truckSize))