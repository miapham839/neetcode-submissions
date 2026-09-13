# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            # Base case
            if not root:
                return [True, 0]
            
            # Condition: Each subtrees are balanced, and their height difference <= 1
            left, right = dfs(root.left), dfs(root.right) # Assume the function already works on smaller problems. We know it returns [balanced?, height]
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1 # Check if the current problem is balanced
            return [balanced, 1 + max(left[1], right[1])] # Return in the format we set out to keep our recursion going

        return dfs(root)[0]
