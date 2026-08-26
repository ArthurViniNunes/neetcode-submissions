class Solution:
    big = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        h = self.diameter(root)        
        return self.big

    def diameter(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        h_l = self.diameter(root.left)
        h_r = self.diameter(root.right)
        h = max(h_l, h_r) + 1
        self.big = max(self.big, h_l+h_r)

        return h