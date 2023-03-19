# LEETCODE PROBLEM:
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if root.left:
            for i in self.DFS(root.left):
                if i.val >= root.val:
                    return False
        if root.right:
            for j in self.DFS(root.right):
                if j.val <= root.val:
                    return False
            
        return self.isValidBST(root.left) and self.isValidBST(root.right)
        ## null case, return True/False, recursion
        
    # returns everything in the tree    
    def DFS(self, root: TreeNode) -> List[TreeNode]:
        visited = []
        need_visit = []
        need_visit.append(root)
        while(need_visit):               
            node = need_visit.pop()
            if node not in visited:
                visited.append(node)
            if node.left:                
                need_visit.append(node.left)
            if node.right:
                need_visit.append(node.right)
        return visited

    
