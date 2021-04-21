
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# Due to the nature of this problem it will not run in a personal environment.

#### Recursive solution (apparently this is trivial)
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output = []
        def dfs(node):
            if not node: return
            output.append(node.val)
            for c in node.children:
                dfs(c)
        dfs(root)
        return output 

###### Iterative solution, it involves reversing the list so that we preform DFS instead of BFS which happens when iterating normally
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        q = deque([root])
        output = []

        while q:
            cand = q.popleft()
            output.append(cand.val)
            for c in reversed(cand.children):
                q.appendleft(c)

        return output