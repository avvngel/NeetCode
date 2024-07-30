#!/usr/bin/env python3

class TrieNode:

    def __init__(self):
        self.children = [None]*26
        self.is_word_end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()     

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_word_end = True
        
    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        return curr.is_word_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        return True

        
        
