# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max_so_far = float("-inf")
        
        def dfs(node, max_so_far):
            if not node:
                return 0
            new_max = max(max_so_far, node.val)
            if node.val >= max_so_far:
                return 1 + dfs(node.left, new_max) + dfs(node.right, new_max)
            else:
                return dfs(node.left, new_max) + dfs(node.right, new_max)
        
        return dfs(root, max_so_far)