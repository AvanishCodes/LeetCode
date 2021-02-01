# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        res = int(0)
        if root.left.val == root.val:
            res += self.longestUnivaluePath(root.left)
        if 
        return res