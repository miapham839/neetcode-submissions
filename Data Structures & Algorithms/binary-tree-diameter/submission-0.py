# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # variable to keep track of max diameter
        self.diam = 0
        # recursively get the height of each node, updating diam along the way
        def height(node):
            # Base case
            if not node:
                return 0
            # recursive case: chưa add 1 vì chưa count root node --> cần tính theo edge đã
            left_height = height(node.left)
            right_height = height(node.right)
            self.diam = max(self.diam, left_height + right_height)
            return 1 + max(left_height, right_height)
        height(root)
        return self.diam
        