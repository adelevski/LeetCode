

# Due to the nature of this problem, it is not possible to run in a personal environemnt 

def removeNthFromEnd(head, n):
    dummy = fast = slow = ListNode(0, next=head)
    
    #move fast ahead n steps
    for _ in range(n):
        fast = fast.next
    
    while fast.next:
        fast = fast.next
        slow = slow.next
        
    slow.next = slow.next.next
    
    return dummy.next


