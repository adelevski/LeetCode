

# Due to the nature of this problem, it will not run in a personal environment 


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    if left == right: return head
    dummy = ListNode(0, next = head)
    prev = dummy
    i = 1
    while i < left:
        prev = prev.next
        i += 1
    
    cur = prev.next
    nx = cur.next
    
    while i < right:
        tmp = nx.next
        nx.next = cur
        cur = nx
        nx = tmp 
        i += 1
        
    prev.next.next = nx
    prev.next = cur
    
    return dummy.next

