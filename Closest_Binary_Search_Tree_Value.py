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
