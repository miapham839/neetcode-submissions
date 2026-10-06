# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        init stack with root
        while stack not empty:
            pop stack
            update max_depth
            if left/right child:
                add itself and current (parent) depth + 1 to stack
                --> you knew what you were stuck on! trust your gut. think about it instead of being anxious and giving up
        return max_depth
        '''
        if not root:
            return 0
        max_depth = 0
        stack = [[root, 1]]
        while stack:
            node = stack.pop()
            max_depth = max(max_depth, node[1])
            if node[0].left:
                stack.append([node[0].left, node[1] + 1])
            if node[0].right:
                stack.append([node[0].right, node[1] + 1])
        return max_depth
        