# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = []
        queue.append(root)
        depth = 0
        while len(queue) != 0:
            numOfNodes = len(queue)
            while (numOfNodes > 0):
                current_node = queue.pop(0)
                if not current_node.left and not current_node.right:
                    depth += 1
                    return depth
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
                numOfNodes -= 1
            depth += 1