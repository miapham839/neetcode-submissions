# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorderTraversalHelper(node):
            if not node:
                return
            inorderTraversalHelper(node.left)
            res.append(node.val)
            inorderTraversalHelper(node.right)
        inorderTraversalHelper(root)
        return res


        