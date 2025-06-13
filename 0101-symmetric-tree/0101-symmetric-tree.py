# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isSameTree(p.left, q.right) and isSameTree(p.right, q.left)
        
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if root.left and root.right:
            return isSameTree(root.left, root.right)
        else:
            return False
                