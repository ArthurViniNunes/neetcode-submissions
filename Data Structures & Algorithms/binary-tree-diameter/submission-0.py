# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getHeight(self, root):
        if root:
            return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        return 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root:
            l, r = self.getHeight(root.left), self.getHeight(root.right)
            total = l + r 
            return max(total, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return 0