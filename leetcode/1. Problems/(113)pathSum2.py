




class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root, targetSum):
    def dfs(root, targetSum, path):
        if root == None: return None
        targetSum -= root.val
        path.append(root.val)
        if root.left == None and root.right == None:
            if targetSum == 0:
                ans.append(path.copy())
        else:
            dfs(root.left, targetSum, path)
            dfs(root.right, targetSum, path)
        path.pop()

    ans = []
    dfs(root, targetSum, [])
    return ans

        



root = [5,4,8,11,null,13,4,7,2,null,null,5,1]
targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]

root = [1,2,3]
targetSum = 5
# Output: []

root = [1,2]
targetSum = 0
# Output: []