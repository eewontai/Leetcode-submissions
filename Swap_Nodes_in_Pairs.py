# LEETCODE PROBLEM:
# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        h = head
        l = ListNode()
        n = l
        list = []
        if h is None:
            return None
        while(h):
            try:
                for i in range(2):
                    list.append(h.val)
                    h = h.next
            except AttributeError:
                n.val = list[0]
                break
            n.val = list[1]
            n.next = ListNode()
            n = n.next
            n.val = list[0]
            if h is None:
                break
            if h.next is not None:
                n.next = ListNode()
                n = n.next
            else:
                n.next = h
                break
            list = []
            
        return l

    
