# from collections import defaultdict

class Node:
    def __init__(self, val=None, children=None):
        self.val = val 
        self.children = children


def levelOrder(root):
    d = {}
        
    def dfs(node, level):
        if not node: return
        d.setdefault(level, [])
        d[level].append(node.val)
        if node.children:
            for child in node.children:
                dfs(child, level+1)
    
    dfs(root, 0)
    
    return d.values()

# root = [1,null,3,2,4,null,5,6]
# Output: [[1],[3,2,4],[5,6]]

node = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])

print(levelOrder(node))