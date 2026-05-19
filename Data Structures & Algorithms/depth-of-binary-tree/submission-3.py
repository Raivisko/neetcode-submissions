# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        stack = [(root, 1)]
        depth = 0
        while stack:
            node, d = stack.pop()  # ← LIFO, tas ir DFS
            depth = max(depth,d )
            if node.right: 
                stack.append((node.right, depth + 1))
            if node.left: 
                stack.append((node.left, depth + 1))
            print(depth, node.val)
        return depth
            