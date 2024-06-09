#!/usr/bin/env python3

class ListNode:

    def __init__(self, key = 0, val = 0, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    
    def __init__(self, capacity: int):
        self.struct = {}
        self.capacity = capacity

        self.head, self.tail = ListNode(), ListNode()
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key in self.struct:
            node = self.struct[key]
            value = node.val

            self.remove_from_cache(node)
            self.append_cache(node)
            self.struct[key] = node
           
        else:
            value = -1

        return value
        
    def put(self, key: int, value: int) -> None:
        new_node = ListNode(key=key, val=value)

        if key in self.struct:
            node = self.struct[key]
            self.remove_from_cache(node)

        elif len(self.struct) == self.capacity:
            lru = self.struct[self.head.next.key]
            self.remove_from_cache(lru)
            del self.struct[lru.key]
        
        self.append_cache(new_node)
        self.struct[key] = new_node
        
    def remove_from_cache(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev, node.next = None, None

    def append_cache(self, node):
        prev = self.tail.prev
        node.prev, node.next = prev, self.tail
        prev.next = node
        self.tail.prev = node
        
    
