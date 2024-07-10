#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque

        q = deque()
        if root: q.append(root)
        
        res = []
        while q:
            rightmost = None

            for _ in range(len(q)):
                node = q.popleft()
                rightmost = node

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            res.append(rightmost.val)
        return res
