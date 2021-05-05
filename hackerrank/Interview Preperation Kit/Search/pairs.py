

# k = 1
# arr = [1, 2, 3, 4]
# #     [1, 2, 3]
# # Output = 3

# k = 2
# arr = [1, 5, 3, 4, 2]
# #     [1, 2, 3, 4, 5]
# #     [1, 2, 3]
# # Output = 3

k = 2
arr = [1, 3, 5, 8, 6, 4, 2]
#     [1, 2, 3, 4, 5, 6, 8]
#     [1, 2, 3, 4, 6]
# Output = 5

# Two pointer method, naive approach too slow
def pairs(k, arr):
    N = len(arr)
    arr.sort()
    count = 0
    left = 0
    right = 1
    while right < N:
        val = arr[right] - arr[left]
        if val == k:
            count += 1
            left += 1
            right += 1
        elif val < k:
            right += 1
        elif val > k:
            left += 1
            if left == right:
                right += 1
    return count   

print(pairs(k, arr))