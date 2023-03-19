# LEETCODE PROBLEM:

# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        a = []
        if root:
            a += self.inorderTraversal(root.left)
            a.append(root.val)
            a += self.inorderTraversal(root.right)
            
            
#        while(root):
#            root = root.left
#        a.append(root)
        
        
        
        return a

    
