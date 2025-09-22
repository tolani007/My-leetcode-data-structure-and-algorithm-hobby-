class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(0, head)   # point dummy directly at head
        current = dummy
        while current.next:          # look ahead at the node we might delete
            if current.next.val == val:
                current.next = current.next.next   # skip the matching node
            else:
                current = current.next             # advance normally
        return dummy.next
