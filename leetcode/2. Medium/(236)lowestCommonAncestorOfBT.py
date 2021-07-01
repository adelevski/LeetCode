
# Due ro the nature of this problem, it will not run in a personal environment

#  Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowest(root, p, q):
    self.ans = None

    def dfs(node):
        if not node:
            return False
        left = dfs(node.left)
        right = dfs(node.right)
        cur = node == p or node == q
        if (left and right) or (cur and right) or (cur and left):
            self.ans = node
            return
        return left or right or cur
    
    dfs(root)
    return self.ans

print(lowest(root, p, q))

