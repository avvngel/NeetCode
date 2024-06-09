#!/usr/bin/env python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reorderList1(self, head: Optional[ListNode]) -> None:
    """
    Space Complexity O(1) solution
    """
        
        # Find middle of linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half of linked list
        prev = None
        curr = slow.next
        slow.next = None # nullify end of left list

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        left, right = head, prev
        
        # Assemble final list
        while left and right:
            next_left, next_right = left.next, right.next
            left.next = right
            right.next = next_left
            left, right = next_left, next_right

    def reorderList2(self, head: Optional[ListNode]) -> None:
    """
    Uses an array and has space complexity O(n)
    """
        
        arr = []
        node = head

        # Store nodes in an array
        while node:
            next_node = node.next # cache next_node
            arr.append(node)      # add to array
            node.next = None      # nullify next ptr
            node = next_node      # step forward through list

        node = head
        l, r = 1, len(arr)-1

        # Assemble re-ordered list using 2 pointers
        while l < r:
            node.next = arr[r]
            node.next.next = arr[l]
            l += 1
            r -= 1
            node = node.next.next
        if l == r: # For odd length linked lists
            node.next = arr[r]
        
            

            

          
        
        
