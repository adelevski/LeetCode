

# Due to the nature of this problem, it will not run in a personal environment




def lowestCA(root, p, q):
    small = min(p.val, q.val)
    large = max(p.val, q.val)
    while root:
        if root.val > large:  # p, q belong to the left subtree
            root = root.left
        elif root.val < small:  # p, q belong to the right subtree
            root = root.right
        else:  # Now, small <= root.val <= large -> This is the LCA between p and q
            return root
    return None


