


class ListNode:
    def __ini__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    prev = None
    nxt = None
    curr = head
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    head = prev
    return head






