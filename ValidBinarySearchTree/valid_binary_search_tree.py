# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, lb, ub):
            if not root:
                return True
            if not lb < root.val < ub:
                return False
            return helper(root.left, lb, root.val) and helper(root.right, root.val, ub)
        return helper(root, -1001, 1001)


