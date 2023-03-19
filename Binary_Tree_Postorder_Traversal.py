# LEETCODE PROBLEM:
# Given the root of a binary tree, return the postorder traversal of its nodes' values.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        node = root
        
        if not root:
            return
        
        else: # not 'while node'
            if node.left:
                res += self.postorderTraversal(node.left)
            if node.right:
                res += self.postorderTraversal(node.right)
            res.append(node.val)
            
            
        return res

    
