
# nums1 = [1,2,2,1]
# nums2 = [2,2]
# Output: [2,2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
# Output: [4,9]




def intersect(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    d1 = {}
    output = []
    for i in range(n1):
        d1.setdefault(nums1[i], 0)
        d1[nums1[i]] += 1
    for i in range(n2):
        if nums2[i] in d1.keys():
            output.append(nums2[i])
            d1[nums2[i]] -= 1
            if d1[nums2[i]] == 0:
                d1.pop(nums2[i])
    return output




print(intersect(nums1, nums2))