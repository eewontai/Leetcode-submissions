# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        list = []
        while(head):
            list.append(head.val)
            head = head.next
            
        del list[-n]
        #node = ListNode()
        if len(list)==0:
            return None

        node = ListNode()
        n = node
        for i in range(len(list)):
            n.val = list[i]
            if i != len(list)-1:
                n.next = ListNode()
                n = n.next
            
            
        return node
