#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest_recursive(self, root: Optional[TreeNode], k: int) -> int:
    """
    Recursive Solution
    """
        soln = None

        def helper(node):
            nonlocal k, soln

            if not node:
                return 

            helper(node.left)
            k -= 1

            if k == 0:
                soln = node.val
            else:
                helper(node.right)

        helper(root)
        return soln

    def kthSmallest_iterative(self, root: Optional[TreeNode], k: int) -> int:
    """
    Iterative solution
    """
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0: return node.val
            node = node.right


