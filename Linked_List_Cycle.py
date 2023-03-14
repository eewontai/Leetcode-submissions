# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        n = set()
        while(head):
            n.add(head)
            head = head.next
            if head in n:
                return True
        return False
