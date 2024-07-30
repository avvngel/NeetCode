#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    
        if not inorder:
            return None

        subroot = TreeNode(val = preorder[0])
        root_idx = inorder.index(preorder[0])
        
        
        # Split lists into subtree lists
        l_subtree_inorder = inorder[:root_idx]
        r_subtree_inorder = inorder[root_idx+1:]
        nl_nodes = len(l_subtree_inorder) # number of left-subtree nodes
        
        l_subtree_preorder = preorder[1:nl_nodes+1]
        r_subtree_preorder = preorder[nl_nodes+1:]

        # Get left and right children
        subroot.left = self.buildTree(l_subtree_preorder, l_subtree_inorder)
        subroot.right = self.buildTree(r_subtree_preorder, r_subtree_inorder)

        return subroot

