


# nums1 = [1, 3]
# nums2 = [2]
# # Output = 2

nums1 = [1, 2]
nums2 = [3, 4]
# Output = 2.500

def findMedianSortedArrays(nums1, nums2):
    merged, ptr1, ptr2 = [], 0, 0
    while ptr1 < len(nums1) and ptr2 < len(nums2):
        if nums1[ptr1] < nums2[ptr2]:
            merged.append(nums1[ptr1])
            ptr1 += 1
        else: 
            merged.append(nums2[ptr2])
            ptr2 += 1
    while ptr1 < len(nums1):
        merged.append(nums1[ptr1])
        ptr1 += 1
    while ptr2 < len(nums2):
        merged.append(nums2[ptr2])
        ptr2 += 1
    N = len(merged)
    if N%2 == 0:
        left = N//2 - 1
        right = N//2
        return (merged[left] + merged[right]) / 2
    else:
        mid = N // 2 
        return merged[mid]

print(findMedianSortedArrays(nums1, nums2))

# N = 4
# print(N//2)