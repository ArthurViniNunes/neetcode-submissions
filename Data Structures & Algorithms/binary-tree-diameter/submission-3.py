# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        big, _ = self.diameter(root)        
        return big

    def diameter(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0, 0
        
        big_l, h_l = self.diameter(root.left)
        big_r, h_r = self.diameter(root.right)
        h = max(h_l, h_r) + 1
        big = max(big_l, big_r, h_l+h_r)

        return big, h