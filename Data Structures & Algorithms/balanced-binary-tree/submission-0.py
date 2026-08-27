# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root: Optional[TreeNode]):
            if root == None:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)

            if l < 0 or r < 0:
                return -1
            
            if abs(l-r) > 1:
                return -1
            
            return 1+max(l,r)
        
        return dfs(root) >= 0