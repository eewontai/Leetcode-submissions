# LEETCODE PROBLEM:
# Given a singly linked list L: L0→L1→…→Ln-1→Ln, reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# You may not modify the values in the list's nodes, only nodes itself may be changed.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        sent = ListNode(next = head)
        st = sent
        h = head
        
        while(h):
            stack.append(h)
            h = h.next
        
        while(stack):    # st and/or stack
            st.next = stack.pop(0)
            st = st.next
            if stack:
                st.next = stack.pop()
                st = st.next
        st.next = None

        
