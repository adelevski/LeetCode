from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

def buildTree(preorder, inorder):
    p = deque(preorder)
    N = len(preorder)

    lookup = {v:i for i,v in enumerate(inorder)}
    def rec(start, end):
        if start > end:
            return None
        else:
            cand = p.popleft()
            root = TreeNode(cand)
            middle = lookup[cand]
            root.left = rec(start, middle-1)
            root.right = rec(middle+1, end)
            return root
        
    return rec(0,N-1)


print(buildTree(preorder, inorder))

