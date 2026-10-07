# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            nonlocal res
            # Base case
            if not root:
                return 0
            # recursive cases
            left = dfs(root.left)
            right = dfs(root.right)
            # update diameter
            res = max(res, left + right)
            # return to keep the dfs going + return correct heights for upper diameter calculations
            return 1 + max(left, right)
        dfs(root)
        return res