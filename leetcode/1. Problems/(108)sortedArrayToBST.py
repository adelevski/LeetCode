# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]

# Due to the nature of this problem, it will not run in a personal environment
def sortedArrayToBST(nums):
    if len(nums) == 0:
        return None
    
    mid = len(nums) // 2
    left = self.sortedArrayToBST(nums[0:mid])
    right = self.sortedArrayToBST(nums[mid + 1:])
    node = TreeNode(nums[mid], left, right)
    return node



