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

    
