#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, branch_max):
            if not node:
                return 0
                        
            branch_max = max(branch_max, node.val)
            count = 1 if node.val == branch_max else 0
            count += helper(node.left, branch_max)
            count += helper(node.right, branch_max)
            return count

        return helper(root, root.val)

