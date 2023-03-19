# LEETCODE PROBLEM: 
# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
# Note:
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        v = root.val
        while(root):
            if root.val > target:
                if abs(v-target) > abs(root.val-target):
                    v = root.val
                root = root.left
            elif root.val < target:
                if abs(v-target) > abs(root.val-target):
                    v = root.val
                root = root.right
            else:
                return root.val
        return v

    
