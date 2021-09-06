
# due to the nature of this problem, it will not run in a personal environment

# Input: [0,0,null,0,0]
# Output: 1
# Explanation: One camera is enough to monitor all nodes if placed as shown.


# Input: [0,0,null,0,null,0,null,null,0]
# Output: 2
# Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.output = 0
        def dfs(node):
            # camera, monitor
            if not node:
                return False,True
            c1,m1 = dfs(node.left)
            c2,m2 = dfs(node.right)
            
            camera,monitor = False,False
            if c1 or c2:
                monitor = True
            if not m1 or not m2:
                camera = True
                self.output += 1
                monitor = True
            return camera,monitor
            
        c, m = dfs(root)
        if not m: return self.output + 1
        
        return self.output