from itertools import combinations


# nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

# nums = [0]
# Output: [[],[0]]

nums = [4,4,4,1,4]
# Output: [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]

# My version
def subsetsWithDup(nums):
    n = len(nums)
    output = []
    st = set()
    for i in range(n+1):
        combo = set(combinations(nums, i))
        combo_list = []
        for item in combo:
            lst = sorted(list(item))
            combo_list.append(tuple(lst))
        combo_set = set(combo_list)
        for item in combo_set:
            output.append(list(item))
    return output


# Crazy one liner version of my method
def subset2(nums):
    return [list(k) for i in range(len(nums)+1) for k in set([tuple(sorted(list(j))) for j in set(combinations(nums, i))])]



print(subsetsWithDup(nums))
print(subset2(nums))
