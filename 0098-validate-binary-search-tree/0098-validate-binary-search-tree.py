# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        floor = float("-inf")
        ceiling = float("inf")

        def DFS(node, floor, ceiling):
            if not node:
                return True

            if not floor < node.val < ceiling:
                return False

            return DFS(node.left, floor, node.val) and DFS(node.right, node.val, ceiling)
        
        return DFS(root, floor, ceiling)
        