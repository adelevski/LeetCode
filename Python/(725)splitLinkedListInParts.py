# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

      
head = [1,2,3]
k = 5
# Output: [[1],[2],[3],[],[]]



def splitListToparts(head, k):
    cur = head
    N = 0
    while cur:
        cur = cur.next
        N += 1
    d, r = divmod(N, k)

    ans = []
    cur = head
    for i in range(k):
        head = cur
        for j in range(d + (i < r) - 1):
            if cur: cur = cur.next
        if cur:
            cur.next, cur = None, cur.next
        ans.append(head)
    return ans




print(splitListToparts(head, k))