# Due to the nature of this problem, it will not run in a personal env

def pruneTree(root):
    def dfs(node):
        if not node: return True
        left, right = dfs(node.left), dfs(node.right)
        if left: node.left = None
        if right: node.right = None
        return left and right and node.val == 0
    
    return root if not dfs(root) else None