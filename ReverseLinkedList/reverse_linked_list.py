#!/usr/bin/env python3

class Solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Recursive solution
        """
        def helper(self, node):
            if not node.next:
                return node, node
            next_node, new_head = self.reverseList_helper(node.next)
            node.next = None
            next_node.next = node
            return node, new_head

        if not head:
            return head
        _, new_head = self.helper(head)
        return new_head

    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iterative solution
        """
        current = head
        prev = None
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
                    
        return prev
