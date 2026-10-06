# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # If root is null, return none
        if not root:
            return None
        # Swap the node's left and right pointers.
        root.left, root.right = root.right, root.left

        # Recursively call dfs on the new left child.
        self.invertTree(root.left)
        # Recursively call dfs on the new right child.
        self.invertTree(root.right)

        # return root node (with all descendant nodes inverted)
        return root