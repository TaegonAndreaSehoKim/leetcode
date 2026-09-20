# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        stack = []
        current = root
        result = root
        while k != 0:
            while current:
                stack.append(current)
                current = current.left
            result = stack.pop()
            current = result.right
            k -= 1

        return result.val