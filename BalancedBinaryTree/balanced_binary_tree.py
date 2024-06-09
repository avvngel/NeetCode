# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return True, 0

            l_bool, l_depth = helper(node.left)
            r_bool, r_depth = helper(node.right)

            balanced = (l_bool and r_bool
                        and (abs(l_depth - r_depth) <= 1))

            return balanced, 1 + max(l_depth, r_depth)
            
        ans, _ = helper(root)
        return ans


