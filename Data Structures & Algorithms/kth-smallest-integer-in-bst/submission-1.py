# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Optimal solution
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        res = 0

        def inorder(node):
            nonlocal count
            nonlocal res
            if not node or count >= k:
                return
            # Traverse left
            inorder(node.left)
            # Count current node
            count += 1
            if count == k:
                res = node.val
            # Traverse right
            inorder(node.right)
        
        inorder(root)
        return res
