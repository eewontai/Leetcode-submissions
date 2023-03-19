# LEETCODE PROBLEM:
# Given the root of a binary tree, return the preorder traversal of its nodes' values.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        stack = []
        node = root
                
        if root is None:
            return None
        
        res.append(root.val)

        while(node or stack):
            if node is not None:
                stack.append(node)
                node = node.left
                try:
                    res.append(node.val)
                except AttributeError:
                    continue

            else:
                node = stack.pop()
                node = node.right
                try:
                    res.append(node.val)
                except AttributeError:
                    continue
        
        return res
    
