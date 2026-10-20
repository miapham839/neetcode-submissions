# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    # Base case
        if not root:
            return None
        # Shrink 
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        # Combine
        root.left = right
        root.right = left
        # Contract
        return root
