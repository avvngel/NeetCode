#!/usr/bin/env python3

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return None
        head = Node(val = node.val)
        node_to_copy = {node: head}
        visited = set()
        stack = [(node, head)]
        while stack:
            curr, copy = stack.pop()
            if curr in visited:
                continue
            visited.add(curr)
            for nhb in curr.neighbors:
                print(nhb.val)
                if nhb not in node_to_copy:
                    node_to_copy[nhb] = Node(val = nhb.val)
                nhb_copy = node_to_copy[nhb]
                copy.neighbors.append(nhb_copy)
                stack.append((nhb, nhb_copy))
        return head
            
        
        
