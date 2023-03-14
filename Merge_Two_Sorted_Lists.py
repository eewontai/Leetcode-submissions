# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        h = head
        
        while(l1 and l2):
            if l1.val <= l2.val:
                h.next = l1
                l1 = l1.next
            else:
                h.next = l2
                l2 = l2.next
            h = h.next
                            
        h.next = l1 if l1 is not None else l2
        return head.next
