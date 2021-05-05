



arr = [3, 1, 3, 4, 2]
#     T,H
#               T  H
#               H  T
#      T     H

def findDuplicates(nums):
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        print(f"tort = {tortoise}, hare = {hare}")
        if tortoise == hare:
            print(f"breaking")
            break
    
    ptr1 = nums[0]
    ptr2 = tortoise
    print(f"initial ptr1={ptr1}, ptr2 = {ptr2}")
    while ptr1 != ptr2:
        print(f"new ptr1 = {nums[ptr1]}, ptr2 = {nums[ptr2]}")
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    print(f"final ptr1 = {ptr1}")

    return ptr1

print(findDuplicates(arr))