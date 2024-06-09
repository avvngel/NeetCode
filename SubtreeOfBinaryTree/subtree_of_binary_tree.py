#!/urs/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isSameTree(self, node1, node2):
        if not node1 and not node2:
            return True

        if node1 and node2 and node1.val == node2.val:
            left_same = self.isSameTree(node1.left, node2.left)
            right_same = self.isSameTree(node1.right, node2.right)
            return left_same and right_same

        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot)
                or self.isSubtree(root.right, subRoot))

