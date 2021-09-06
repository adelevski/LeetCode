
# Due to the nature of this problem, it will not run in a personal environment


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = [2,1,3]
# Output: true

# root = [5,1,4,null,null,3,6]
# Output: false

def isValidBST(root):
    
    def dfs(lower,upper,node):
        if not node: return True
        elif node.val<=lower or node.val>=upper:
            return False
        else:
            return dfs(lower,node.val, node.left) and dfs(node.val, upper, node.right)
    
    return dfs(float('-inf'),float('inf'),root)

print(isValidBST(root))