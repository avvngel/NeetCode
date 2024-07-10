#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        
        queue = deque()
        if root: queue.appendleft(root)
        
        res = []
        
        while queue:
            level_vals = []

            for _ in range(len(queue)):
                node = queue.pop()
                level_vals.append(node.val)
                if node.left: queue.appendleft(node.left)
                if node.right: queue.appendleft(node.right)
            res.append(level_vals)
        return res
