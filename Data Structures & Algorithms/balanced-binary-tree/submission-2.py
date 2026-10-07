# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            # Base case
            if not root:
                return 0
            # Recursive case
            left = height(root.left)
            right = height(root.right)
            if (left == -1) or (right == -1):
                return -1
            # Check if balanced
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        return height(root) != -1

        