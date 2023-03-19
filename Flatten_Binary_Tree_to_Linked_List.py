# LEETCODE PROBLEM: 
# Given the root of a binary tree, flatten the tree into a "linked list":
# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ## stack = []
        r = root
        if not root:
            return
        ## modify root in-place, use r as variable
        
        self.flatten(root.left)
        self.flatten(root.right)
        
        r = r.left
        if r is not None:
            while(r.right):
                r = r.right
            r.right = root.right            

            root.right = root.left
            root.left = None

            
