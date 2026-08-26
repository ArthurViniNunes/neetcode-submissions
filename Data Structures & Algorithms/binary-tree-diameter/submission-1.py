# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def H(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = self.H(root.left) + 1 
        r = self.H(root.right) + 1
        return max(l, r)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        h = self.H(root.left) + self.H(root.right)
        return max(h, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))