# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        a = head
        while(head):
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
            
        return a
    
        """
        if head == None:
            return head
        
        current = head.next
        prev = head
        
        while current:
            if current.val == prev.val:
                prev.next = current.next
                current = current.next
            else:
                current = current.next
                prev = prev.next
        
        return head
        
