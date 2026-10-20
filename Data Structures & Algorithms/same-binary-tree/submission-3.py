# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        - Recursive case: isSameTree takes 2 nodes (the root of 2 subtrees) --> returns if the 2 subtrees are the same (T/F)
        - Base case: 
            - both are null: return True
            - both are not null and their values are the same: 
                check if left subtrees are the same AND right subtrees are the same
            - botn are not null and their values are diff: return False
        '''
        # Base case:
        if (not p and q) or (not q and p):
            return False
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        elif p and q and p.val != q.val:
            return False
