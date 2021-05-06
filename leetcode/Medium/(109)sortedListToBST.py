
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

head = [-10,-3,0,5,9]
# Output = [0,-3,9,-10,null,5]

# Due to the nature of this problem, it will not run in a personal environment
def sortedListToBST(head):
    n = 0
    cur = head
    while cur:
        cur = cur.next
        n+=1
    self.head = head
    def rec(st,end):
        if st>end: return None
        #left
        mid = (st+end)//2
        left = rec(st,mid-1)
        #root
        root = TreeNode(self.head.val)
        self.head = self.head.next
        root.left = left
        #right
        root.right = rec(mid+1, end)
        return root

    return rec(0, n-1)

        